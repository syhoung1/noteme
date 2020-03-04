from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.
def home(request):
    user = User.objects.first()
    topic = Topic.objects.get(user=User.objects.first())
    notes = Note.objects.all()
    vocab = Vocab.objects.filter(topic__user__name="Steven")
    return render(
        request = request,
        template_name = "main/home.html",
        context={
            "user": user,
            "topic": topic,
            "notes": notes,
            "vocab": vocab,
        }
    )
