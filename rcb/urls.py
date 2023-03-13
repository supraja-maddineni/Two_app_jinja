from rcb.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('First_rcb/',First_rcb,name='First_rcb'),
    path('Second_rcb/',Second_rcb,name='Second_rcb')

]