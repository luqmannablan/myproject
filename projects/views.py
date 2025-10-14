from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.


def projects_list(request):

    projectItem = Project.objects.all().order_by()
    return render(request, 'projects/projects_list.html', {'projects': projectItem})
