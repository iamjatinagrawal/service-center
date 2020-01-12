from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class ServiceCenter(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# class Customer(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)


# class UserProfileInfo(models.Model):
#     user = models.OneToOneField(User,on_delete=models.PROTECT)
#     portfolio_site = models.URLField(blank=True)
#     protfolio_pic = models.ImageField(upload_to='profile_pics',blank=True)


    # def __str__(self):
    #     return self.user.username


class Ticket(models.Model):
    ticketID = models.PositiveIntegerField(unique=True,verbose_name="Ticket ID")
    receivedOn = models.DateField(verbose_name="Date")
    customerFirstName = models.CharField(max_length=100,verbose_name="First Name")
    customerLastName = models.CharField(max_length=100, verbose_name="Last Name")
    brand = models.CharField(max_length=20, verbose_name="Brand")
    product = models.CharField(max_length=100, verbose_name="Product Name")
    serialNumber = models.CharField(max_length=100, verbose_name="Serial Number")
    phoneNumber = models.PositiveIntegerField(verbose_name="Contact Number")
    emailID = models.EmailField(verbose_name="Email")
    status = models.CharField(max_length=50, default="Pending", verbose_name="Status")

    def __str__(self):
        return str(self.ticketID)

    def get_absolute_url(self):
        return reverse('support_ticket:stl')
        #return reverse('ticket_detail',kwargs={'pk':self.pk})

# def incrementalTicketID():
#     lastTicketID = Ticket.objects.all().order_by('id').last()
#     if not lastTicketID:
#         return 'ND'+str(1)