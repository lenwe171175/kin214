from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from kin214.settings import LOGIN_URL
from .forms import InscriptionForm, MonProfilForm
from .models import Utilisateur

# Create your views here.

def page_not_found_view(request, exception):
    return render(request, "404.html", status=404)

@login_required
def index(request):
    return render(request, "users/index.html")

def inscription(request):
    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data["password"]
            password2 = form.cleaned_data["password_validation"]
            if password1 and password2 and password1 != password2:
                messages.warning(
                    request, "Les mots de passe renseignés sont différents"
                )
                return redirect(inscription)
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            messages.success(request, "Création du compte réussie")
            return redirect(LOGIN_URL)
        else:
            messages.error(
                request, "Une erreur est survenue lors de la création du compte"
            )
    else:
        form = InscriptionForm()
    return render(request, "users/inscription.html", {"form": form})

@login_required
def monprofil(request):
    user = Utilisateur.objects.get(pk=request.user.pk)
    if request.method == "POST":
        form = MonProfilForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Modification(s) réussie(s)")
            return redirect(monprofil)
        else:
            messages.error(request, "Une erreur est survenue lors de la modification")
            return redirect(monprofil)
    else:
        form = MonProfilForm(instance=user)
    return render(request, "users/monprofil.html", {"form": form})

@login_required
def annuaire(request):
    utilisateur_liste=Utilisateur.objects.filter(is_active=True)
    return render(request, "users/annuaire.html", { "list" : utilisateur_liste})