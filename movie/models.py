from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Actor(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.TextField(null=True)
    nickname = models.CharField(max_length=300, null=True)
    def __str__(self):
        return self.nickname

class Director(models.Model):
   
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    most_famous_movie = models.TextField(null=True)
    def __str__(self):
        return self.most_famous_movie