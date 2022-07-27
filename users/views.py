from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from kin214.settings import LOGIN_URL
from .forms import InscriptionForm

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