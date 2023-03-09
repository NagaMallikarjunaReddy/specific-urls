from django.urls import path
from rcb.views import *
app_name='nothing'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('sharma/',sharma,name='sharma'),
]