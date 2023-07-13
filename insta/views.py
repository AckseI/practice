from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

from .models import PostImage

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'insta/pages/index.html'
    context_object_name = 'object_list'
    # context['posts_count'] = models.PostImage.objects.count()

    def get_queryset(self):
        """Return the last five published questions."""
        return PostImage.objects.order_by('-pub_date')

class SubmitView(generic.DetailView):
    model = PostImage
    template_name = "insta/submit.html"

class ResultView(generic.DetailView):
    model = PostImage
    template_name = "insta/result.html"

class DetailView(generic.DetailView):
    model = PostImage
    template_name = "insta/detail.html"