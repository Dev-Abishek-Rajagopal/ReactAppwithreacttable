'''
Created on 27-MAR-2021

@author: Abishek Rajagopal
'''

from django.contrib.auth.models import User
from djongo import models
from django.conf import settings
from fernet_fields import EncryptedTextField
from unixtimestampfield.fields import UnixTimeStampField


class Green_Owner(models.Model):

    user = models.ForeignKey(User, related_name='Green_User',on_delete=models.CASCADE)

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    username = models.CharField(max_length=200,unique=True)

    password = EncryptedTextField(max_length=1000)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    email = models.CharField(max_length=200,unique=True)

    active = models.BooleanField(default=False)
    contact =  models.CharField(max_length=200,null=True)
    FB_link = models.CharField(max_length=200,null=True)
    Twitter_link = models.CharField(max_length=200, null=True)
    Insta_link = models.CharField(max_length=200, null=True)
    Linkedin_link = models.CharField(max_length=200, null=True)
    social_media = models.CharField(max_length=200, null="None")
    social_media_link = models.CharField(max_length=200, null=True)
    privacy_info = models.IntegerField(default=0)

    publist = UnixTimeStampField(auto_now=True, null=True)
    dp = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        self.email = self.email.lower()
        self.country = self.country.lower()
        self.city = self.city.lower()
        return super(Green_Owner, self).save(*args, **kwargs)


class Green_Business(models.Model):

    name = models.CharField(max_length=200)
    Website = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    Address = models.TextField()
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    maplocation = models.TextField()

    dp = models.TextField(null=True, blank=True)

    owner = models.ForeignKey(Green_Owner, on_delete=models.CASCADE,related_name='BusinessOwner')

    desc = models.TextField()

    email = models.CharField(max_length=200, unique=True)

    contact = models.CharField(max_length=200, null=True)
    FB_link = models.CharField(max_length=200, null="None")
    Twitter_link = models.CharField(max_length=200, null=True)
    Insta_link = models.CharField(max_length=200, null=True)
    Linkedin_link = models.CharField(max_length=200, null=True)
    social_media = models.CharField(max_length=200, null="None")
    social_media_link = models.CharField(max_length=200, null=True)

    active = models.BooleanField(default=False)

    BusinessFrom = UnixTimeStampField(null=True)
    publist = UnixTimeStampField(auto_now=True, null=True)



    def save(self, *args, **kwargs):

        self.email = self.email.lower()
        self.country = self.country.lower()
        self.city = self.city.lower()
        self.landmark = self.landmark.lower()
        return super(Green_Business, self).save(*args, **kwargs)