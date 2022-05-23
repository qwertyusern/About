from django.shortcuts import render,redirect
from .models import *
def home(request):
   return render(request, "home.html")

def about(request):
   return render(request, "about.html")

def maqola(request,pk):
   return render(request, "maqola.html", {"maqola":Maqola.objects.get(id=pk)})

def blog(request):
   m=Maqola.objects.all()
   return render(request, "blog.html", {'maqola':m})

def inter(request):
   i=Intervyu.objects.all()
   for f in i:
      f.link=f.link.replace("watch?v=", "embed/")
   return render(request, "intervyu.html", {'intervyu':i})