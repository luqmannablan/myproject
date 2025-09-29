from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.posts_list, name="list"),
    path('new-post/', views.posts_new, name="new-post"),
    # catches anything below for the slug
    path('<slug:slug>', views.posts_page, name="page"),
]
