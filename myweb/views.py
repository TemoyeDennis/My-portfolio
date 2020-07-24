from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Project, Service


# Create your views here.
def home(request):
    projects = Project.objects.all()
    Services = Service.objects.all()
    return render(request, 'index.html', {'projects': projects, 'Services': Services})
