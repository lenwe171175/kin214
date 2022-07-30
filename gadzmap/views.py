import json
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from .models import Position

# Create your views here.

class PositionsMapView(TemplateView):
    template_name = "gadzmap/gadzmap.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["positions"] = json.loads(serialize("geojson", Position.objects.using("gadzmap").all()))
        return context