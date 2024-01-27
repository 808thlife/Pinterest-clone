from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    photo = models.ImageField(default= "core/img/av.png", upload_to = "core/img/userslogo")    
    email = models.EmailField(max_length=254)