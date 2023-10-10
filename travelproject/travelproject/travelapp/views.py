from django.shortcuts import render
from django.http import HttpResponse
from .models import Place,Team

# Create your views here.
def demo(request):
    object=Place.objects.all
    obj=Team.objects.all
    return render(request,'index.html',{'results':object,'result':obj})

