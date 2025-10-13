from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):

    company = models.CharField(max_length=75)
    description = models.TextField()
    skills = models.JSONField(default=list)
    slug = models.SlugField()
    date = models.DateField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.company
