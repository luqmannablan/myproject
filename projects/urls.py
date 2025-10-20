from django.urls import path
from . import views


app_name = 'projects'


urlpatterns = [

    path('', views.projects_list, name='projects-lists'),
    path('new-project/', views.projects_form, name='projects-form')
]
