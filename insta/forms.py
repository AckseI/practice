from django import forms
from django.forms import ModelForm
from .models import PostImage

class PostImageForm(ModelForm):
    class Meta:
        model = PostImage
        fields = ('image_source', 'comment')
        