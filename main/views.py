from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.
def home(request):
    return render(
        request = request,
        template_name = "main/home.html",
        context={
            "users": Users.objects.all(),
            "topics": Topics.objects.all(),
            "notes": Notes.objects.all(),
            "vocab": Vocab.objects.all()
        }
    )
