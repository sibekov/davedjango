from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def homepage(request):
    #return HttpResponse("Hello World! I am home")
    return render(request,'home.html')

def about(request):
    #return HttpResponse("My About page.")
    return render(request,'about.html')