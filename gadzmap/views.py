import json
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib import messages
from gadzmap.forms import MaLocalisationForm
from .models import Position
from users.models import Utilisateur
from users.views import index
from django.contrib.auth.decorators import login_required

# Create your views here.

class PositionsMapView(TemplateView):
    template_name = "gadzmap/gadzmap.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["positions"] = json.loads(serialize("geojson", Position.objects.using("gadzmap").all()))
        return context

@login_required
def malocalisation(request):
    user=Utilisateur.objects.get(pk=request.user.pk)
    try:
        instance=Position.objects.using("gadzmap").get(userid=request.user.pk)
    except:
        instance=None
    if request.method == "POST":
        form=MaLocalisationForm(request.POST, instance=instance)
        if form.is_valid():
            userloc=form.save(commit=False)
            userloc.description=user.first_name + " " + user.last_name
            userloc.userid=user.pk
            userloc.save(using="gadzmap")
            messages.success(request, "Modification(s) réussie(s)")
            return redirect(index)
        else:
            messages.error(request, "Une erreur est survenue")
    else:
        form = MaLocalisationForm(instance=instance)
    return render(request, "gadzmap/malocalisation.html", {"form":form})