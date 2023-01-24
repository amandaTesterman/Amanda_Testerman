from django.db import models
from phone_field import PhoneField
from django.db.models import Model



# Create your models here.
class Comment(Model):
    comment = models.TextField()

class ContactInfo(Model):
   name = models.CharField(max_length=35) 
   phone = PhoneField(blank=True, help_text='Contact phone number')
#  phone = PhoneNumberField(null=True)
#  phone = PhoneNumberField(null=False, blank=False, unique=True)
   email = models.EmailField(max_length=254 )


   '''
PhoneField accepts standard options for a Django CharField. By default it sets max_length=31. Feel free to override this, set blank=True, etc. as you would otherwise.

There is one special argument, E164_only=False, which adds a form validator to only accept numbers in the E164 format (currently, only supported for US phone numbers).

User {{ obj.name }} has phone number {{ obj.phone }}
   '''