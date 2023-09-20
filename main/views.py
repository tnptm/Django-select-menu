from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProjectsSelectForm, ArticleForm
# Create your views here.

def index(request):
    form = None
    form_article = None
    proj = ""
    title = ""
    pub_date = ""
    template_data = None

    if request.method == 'POST':
        # popdown menu
        form = ProjectsSelectForm(request.POST)
        if form.is_valid():
            # Here is how to handle request parameters like redirecting to another projects-specific page
            selected_project = form.cleaned_data['projects']
            proj = selected_project
        
        # article data
        form_article = ArticleForm(request.POST)
        if form_article.is_valid():
            title = form_article.cleaned_data['title']
            pub_date = form_article.cleaned_data['pub_date']
            
    else:
        form = ProjectsSelectForm()
        form_article = ArticleForm()
    if (proj and title):
        template_data = {
            "welcome":"<h1>Hola amigo!</h1>",
            "form": form,
            "article_fields": form_article,
            "proj": proj,
            "article_data": f"Title: '{title}'. Publication date: {pub_date}"
        }
    else:
        template_data = {
            "welcome":"<h1>Hola amigo!</h1>",
            "form": form,
            "article_fields": form_article,
        #    "proj": proj,
        #    "article_data": f"Title: '{title}'. Publication date: {pub_date}"
        }
    return render(request,"index.html",template_data)
