from django import forms
from . import models
from django.contrib.auth.models import User

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = '__all__'


# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())

#     class Meta():
#         model = User
#         fields = ('username','email','password')

# class UserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = models.UserProfileInfo
#         fields = ('portfolio_site','profile_pic')