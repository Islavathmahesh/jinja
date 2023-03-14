from django.shortcuts import render

# Create your views here.
def jinja(request):
    c={'name':'mahesh','age':22}
    return render(request,'jinja.html',context=c)