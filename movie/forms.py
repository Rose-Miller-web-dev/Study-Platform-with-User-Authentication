from django.forms import forms
from .models import Actor, Director
from django.forms import ModelForm

class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'

class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
