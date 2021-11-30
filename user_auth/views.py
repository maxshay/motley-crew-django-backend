from django.shortcuts import render
from django.http import HttpResponse


def home(request):
  return HttpResponse("auth home")


def login(request):
  return HttpResponse("auth login")


def register(request):
  return HttpResponse("auth home")