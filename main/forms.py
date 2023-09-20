from django import forms
from .models import Projects

class ProjectsSelectForm(forms.Form):
    projects = forms.ModelChoiceField(
        queryset=Projects.objects.all(),  # An empty initial queryset
        empty_label="Select a project",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
