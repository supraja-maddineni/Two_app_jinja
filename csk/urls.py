from csk.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('First_csk/',First_csk,name='First_csk'),
    path('Second_csk/',Second_csk,name='Second_csk'),
]