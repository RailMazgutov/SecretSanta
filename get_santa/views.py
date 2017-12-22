from django.shortcuts import render
from .models import Santa, Kid
import random
# Create your views here.

def getMySanta(request):
    santas = []
    for santa in Santa.objects.all():
        #kid= Kid()
        #kid.kid_name = santa.santa_name
        #kid.kid_photo = santa.santa_photo_url
        #kid.save()
        santas.append(santa)
    random.shuffle(santas)
    return render(request, "select_self.html", {"santas": santas})

def getMyKid(request, pk):
    santa = Santa.objects.get(pk=pk)
    kids = []
    for kid in Kid.objects.all():
        if kid.kid_name != santa.santa_name:
            kids.append(kid)

    kid = random.choice(kids)
    kid.delete()
    santa.delete()
    return render(request, "get_kid.html", {"kid": kid})

