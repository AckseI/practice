from django.db import models

# Create your models here.

class PostImage(models.Model):
    def __str__(self):
        return self.comment
    
    image_source = models.ImageField(blank=False, upload_to='images/')
    comment = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
