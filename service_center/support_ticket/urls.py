from django.conf.urls import url
from . import views

app_name = 'support_ticket'

urlpatterns = [

    url(r'^$',views.user_login,name='index'),
    url(r'^stl/',views.SupportTicketList.as_view(),name='stl'),
    url(r'^ticket/(?P<pk>\d+)$', views.TicketDetailView.as_view(), name='ticket_detail'),
    url(r'^create/',views.CreateTicket.as_view(),name='createTicket'),
    url(r'^logout/',views.user_logout,name='logout')

]