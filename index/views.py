from django.shortcuts import render, HttpResponse
from .models import Distro, Artikkeli
from index.forms import PostForm

def index(req):
    return render(req, "index/index.html")

def distro(req):
    distrot = Distro.objects.all()
    return render(req, "index/distrot.html", {'distrot': distrot})

def toinensivu(req):
    artikkelit = Artikkeli.objects.all()
    return render(req, "index/toinensivu.html", {'artikkelit': artikkelit})
