from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse("Home Page (users)")

def contact(request):
  return HttpResponse("Contact Page (users)")

def account(request):
  return HttpResponse("Accont info Page (users)")

