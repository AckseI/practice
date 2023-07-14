from django import forms
from django.forms import ModelForm
from .models import PostImage

class PostImageForm(ModelForm):
    class Meta:
        model = PostImage
        fields = ('image_source', 'comment')
        labels = {
            'image_source': 'Изображение',
            'comment': 'Комментарий',
        }
        widgets = {
            'image_source': forms.FileInput(attrs={'class':"form-control", 'type':"file", 'id':"image", 'name':"image"}),
            'comment': forms.Textarea(attrs={'class':'form-control comment-field'}),
        }
        