

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from FoGApp.views.views import (create_Owner,create_Business,Green_BusinessVeiwSet,Green_OwnerVeiwSet,Get_Business)

owner = Green_OwnerVeiwSet.as_view({
    'get' : 'list_User',

})

owner_id = Green_OwnerVeiwSet.as_view({
    'get' : 'get_User',
    'put': 'update_User',
    'delete': 'delete_User'
})

business = Green_BusinessVeiwSet.as_view({
    'get' : 'list_business',

})

business_id = Green_BusinessVeiwSet.as_view({
    'get' : 'get_business',
    'put': 'update_business',
    'delete': 'delete_business'
})


urlpatterns = [

url(r'^create_owner/$', create_Owner),
url(r'^create_business/$', create_Business),

url(r'^Get_Business/$', Get_Business),

url(r'^owners/$', owner),
url(r'^owners/(?P<pk>\d+)/$', owner_id),

url(r'^business/$', business),
url(r'^business/(?P<pk>\d+)/$', business_id),

]
