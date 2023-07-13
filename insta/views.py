from django.shortcuts import render
from django.views import generic

from .models import PostImage

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'insta/index.html'
    context_object_name = 'object_list'

class SubmitView(generic.DetailView):
    model = PostImage
    template_name = "insta/submit.html"

class ResultView(generic.DetailView):
    model = PostImage
    template_name = "insta/result.html"

class DetailView(generic.DetailView):
    model = PostImage
    template_name = "insta/detail.html"