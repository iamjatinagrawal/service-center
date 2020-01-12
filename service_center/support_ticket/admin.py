from django.contrib import admin
from support_ticket.models import Ticket,ServiceCenter
# Register your models here.

admin.site.register(Ticket)
admin.site.register(ServiceCenter)
# admin.site.register(UserProfileInfo)
#admin.site.register(Customer)