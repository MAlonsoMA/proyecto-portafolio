from django.shortcuts import render

from .models import Project

# Create your views here.
def portfolio(request):
    
    #traer los datos de la base
    projects=Project.objects.all()

    return render(request,'portfolio/portfolio.html', {'projects':projects})