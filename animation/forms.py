from django.forms import ModelForm
from .models import Animation

class AnimationForm(ModelForm):
    class Meta:
        model = Animation
        fields = '__all__'