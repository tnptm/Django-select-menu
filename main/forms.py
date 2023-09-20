from django import forms
# database models from models.py
from .models import Projects
from datetime import date

def date2str():
    """
    Date2str()
    Returns current date as string: 2023-9-20
    """
    t = date.today()
    tf = f"{t.year}-{t.month}-{t.day}"
    return tf

class ProjectsSelectForm(forms.Form):
    projects = forms.ModelChoiceField(
        queryset=Projects.objects.all(),  
        empty_label="Select a project",
        widget=forms.Select(attrs={'class': 'form-control bg-primary text-white'}),
    )

class ArticleForm(forms.Form):
    """
    Article form set (title and pub_date)
    """    
    title = forms.CharField()
    pub_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date','placeholder': 'yyyy-mm-dd' }),
        label="Publication date"
    )

