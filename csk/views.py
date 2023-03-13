from django.shortcuts import render

# Create your views here.
def First_csk(request):
    d={'name':'Supraja'}
    return render(request,'jinja_second.html',context=d)
def Second_csk(request):
    d={'name':'Maddineni'}
    return render(request,'jinja_second.html',context=d)