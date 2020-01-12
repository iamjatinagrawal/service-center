from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView, CreateView,DetailView,UpdateView
from support_ticket.models import Ticket
from . import forms

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SupportTicketList(ListView):
    context_object_name = 'ticketList'
    model = Ticket

    def get_queryset(self):
        return Ticket.objects.order_by('-receivedOn')

class CreateTicket(CreateView):
    form = forms.TicketForm
    model = Ticket
    fields = '__all__'
    #redirect_field_name = 'support_ticket/templates/support_ticket/ticket_list.html'

class TicketDetailView(DetailView):
    model = Ticket

# class TicketUpdateView(UpdateView):
#     form = forms.TicketForm
#     model = Ticket

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('stl'))

@login_required
def special(request):
    return HttpResponse("You are logged in!")


def user_login(request):
    if  request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('support_ticket:stl'))
            else:
                return HttpResponse("Account Not Active")
        
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse ("Invalid login details supplied")
    
    else:
        return render(request,'support_ticket/index.html')