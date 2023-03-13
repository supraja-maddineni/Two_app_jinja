from django.shortcuts import render

# Create your views here.
def First_rcb(request):
    d={'name':'Virat Kohli'}
    return render(request,'jinja_second.html',context=d)
def Second_rcb(request):
    d={'name':'Harshal Patel'}
    return render(request,'jinja_second.html',context=d)