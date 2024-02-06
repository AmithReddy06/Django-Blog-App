from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Home Page of Blog App:Amith")
    return render(request,'homepage.html')
def about(request):
    # return HttpResponse("About Page of Blog")
    return render(request,'about.html')

