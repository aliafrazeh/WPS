from django.shortcuts import render
from django.views.generic import DetailView,CreateView
from .models import ArticleWeb
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    return render(request,template_name="home/home.html")

class DetailWeb(DetailView):
    queryset = ArticleWeb.objects.filter(status=False)
    template_name = "home/detail.html"
    context_object_name = "article"

class CreateWeb(CreateView):
    # queryset = ArticleWeb.objects.all()
    model = ArticleWeb
    template_name = "home/create.html"
    fields = ('title','slug','description','author','image')
    success_url = reverse_lazy("home:home")