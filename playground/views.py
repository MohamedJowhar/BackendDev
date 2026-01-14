from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#request and response object

# def home(request):
#     return HttpResponse("Welcome to the Playground Home Page!")
def home(request):
    return render(request, "Index.html")

def about(request):
    x=1
    y=4
  
    return render(request, "About.html")
