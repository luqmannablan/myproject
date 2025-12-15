from django import forms
from . import models


class createProject(forms.ModelForm):

    class Meta:
        model = models.Project
        fields = ["projectname", "company", "jobtitle",
                  "description", "skills", "startdate", "enddate"]
