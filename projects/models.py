from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):

    company = models.CharField(max_length=75)
    projectname = models.CharField(max_length=75, null=True)
    jobtitle = models.CharField(max_length=75, default="", blank=True)
    description = models.TextField()
    skills = models.JSONField(default=list)
    startdate = models.DateField()
    enddate = models.DateField(null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.company
