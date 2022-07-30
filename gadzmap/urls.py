from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("gadzmap/", login_required(views.PositionsMapView.as_view()), name="gadzmap"),
    path("malocalisation/", views.malocalisation, name="malocalisation")
]
