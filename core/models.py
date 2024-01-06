from django.db import models
from accounts.models import User
# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 24)
    description = models.CharField(max_length=512)
    photo = models.ImageField(upload_to="core/img/")
    viewed = models.IntegerField(default = 0)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} by {self.user}"
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

    def __str__(self):
        return f"like on {self.post} "
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField(max_length = 1024)