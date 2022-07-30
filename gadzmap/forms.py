from django import forms
from .models import Position

class MaLocalisationForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = ["location"]