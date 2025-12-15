from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project
from . import forms

# Create your views here.


def projects_list(request):

    projectItem = Project.objects.all().order_by('-startdate')
    return render(request, 'projects/projects_list.html', {'projects': projectItem})


@login_required(login_url="/users/login/")
def projects_form(request):

    if request.method == 'POST':
        form = forms.createProject(request.POST, request.FILES)
        if form.is_valid():

            newProject = form.save(commit=False)
            newProject.author = request.user
            newProject.save()

            return redirect('projects:projects-lists')
    else:
        form = forms.createProject()

    return render(request, 'projects/projects_form.html', {'form': form})
