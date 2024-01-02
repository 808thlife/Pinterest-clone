from django.db import models

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length = 24)
    description = models.CharField(max_length=512)
    photo = models.ImageField(upload_to="core/img/")
    
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

