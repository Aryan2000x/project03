from django.shortcuts import render
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')