from django.shortcuts import render
from .models import Training,Skill

# Create your views here.
def about(request):
    trainings=Training.objects.all()
    skills=Skill.objects.all()
    return render(request,'about/about.html',{'trainings': trainings,'skills':skills})