from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProjectsSelectForm
# Create your views here.

def index(request):
    form = None
    proj = ""
    if request.method == 'POST':
        form = ProjectsSelectForm(request.POST)
        if form.is_valid():
            # Do something with the selected project, e.g., redirect to a project-specific page
            selected_project = form.cleaned_data['projects']
            proj = selected_project
            # ...
    else:
        form = ProjectsSelectForm()
    
    template_data = {
        "welcome":"<h1>Hola amigo!</h1>",
        "form": form,
        "proj": proj,
    }

    return render(request,"index.html",template_data)