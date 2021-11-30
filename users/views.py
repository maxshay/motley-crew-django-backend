from django.shortcuts import render

def home(request):
  return render(request, "users/index.html")


def contact(request):
  return render(request, "users/contact.html")


def about(request):
  return render(request, "users/about.html")

