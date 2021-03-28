'''
Created on 27-MAR-2021

@author: Abishek Rajagopal
'''

from django.contrib import admin

# Register your models here.

from FoGApp.models import (Green_Business,Green_Owner)

admin.site.register(Green_Business)
admin.site.register(Green_Owner)