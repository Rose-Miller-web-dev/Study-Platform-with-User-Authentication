from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Animation(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #updated = models.DateTimeField(auto_now=True)
    #created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name