from typing import Any
from django.db.models.query import QuerySet
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect

from .models import PostImage
from .forms import PostImageForm

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'insta/pages/index.html'
    context_object_name = 'object_list'
    #context['posts_count'] = models.PostImage.objects.count()#
    def get_queryset(self):
        return PostImage.objects.order_by('-pub_date')

def detail(request, pk):
    post = get_object_or_404(PostImage, pk=pk)
    return render(request, 'insta/pages/detail.html', {'post': post})

def submit(request):
    submitted = False
    if request.method == "POST":
        form = PostImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #post.image_source = form.cleaned_data['image_source']
            post.pub_date = timezone.now()
            post.save()
            return HttpResponseRedirect(f'/insta/success/{post.id}')
    else:
        form = PostImageForm
        if 'submitted' in request.GET:
            submitted = True
    form = PostImageForm
    return render(request, "insta/pages/submit.html", {'form': form, 'submitted': submitted})

def likes(request, pk):
    like = get_object_or_404(PostImage, id=pk)
    like.likes += 1
    like.save()
    return redirect(request.META.get('HTTP_REFERER'))

def success_id(request, pk):
    post = get_object_or_404(PostImage, pk=pk)
    return render(request, 'insta/pages/success.html', {'post': post})