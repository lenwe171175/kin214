from django import forms
from .models import Position

from leaflet.forms.widgets import LeafletWidget

class MaLocalisationForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = ["location"]
        widgets = {'location': LeafletWidget()}
