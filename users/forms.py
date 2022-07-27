from captcha.fields import CaptchaField, CaptchaTextInput
from django import forms
from django.contrib.auth.forms import PasswordResetForm, AuthenticationForm
from .models import Utilisateur

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "validate", "placeholder": "Nom d'utilisateur"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Mot de passe"})
    )

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={"placeholder": "Adresse email"})
    )
    captcha = CaptchaField(
        required=True, widget=CaptchaTextInput(attrs={"placeholder": "Captcha"})
    )

class InscriptionForm(forms.ModelForm):
    password_validation = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirmation du mot de passe"}
        ),
    )
    captcha = CaptchaField(
        required=True,
        widget=CaptchaTextInput(attrs={"placeholder": "Captcha"}),
    )

    class Meta:
        model = Utilisateur
        fields = [
            "username",
            "first_name",
            "last_name",
            "phone",
            "email",
            "password",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "first_name": forms.TextInput(attrs={"placeholder": "Prénom"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Nom de famille"}),
            "phone": forms.TextInput(attrs={"placeholder": "Téléphone"}),
            "email": forms.TextInput(attrs={"placeholder": "Adresse email"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Mot de passe"}),
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        domain = data.split('@')[1]
        domain_list = ["gadz.org"]
        if domain not in domain_list:
            raise forms.ValidationError("Seules les adresses mail Gadz.org sont autorisées")
        return data

    
    def __init__(self, *args, **kwargs):
        super(InscriptionForm, self).__init__(*args, **kwargs)
        self.fields["username"].required = True
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["phone"].required = True
        self.fields["email"].required = True