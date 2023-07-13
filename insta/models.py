from django.db import models

# Create your models here.

class PostImage(models.Model):
    def __str__(self):
        return self.comment
    
    image_source = models.ImageField(upload_to='images/', max_length=100)
    comment = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
