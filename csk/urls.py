from csk.views import *
from django.urls import path
app_name="some"
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('abd/',abd,name='abd'),
]