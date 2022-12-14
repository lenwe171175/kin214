from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path("login/",auth_views.LoginView.as_view(template_name="registration/login.html", form_class=forms.CustomLoginForm),name="login",),
    path( "password_change/",auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"),name="password_change",),
    path("password_change_done/",auth_views.PasswordChangeDoneView.as_view(),name="password_change_done",),
    path("password_reset/",auth_views.PasswordResetView.as_view(form_class=forms.CustomPasswordResetForm),name="password_reset",),
    path("password_reset_done/",auth_views.PasswordResetDoneView.as_view(),name="password_reset_done",),
    path("password_reset_confirm/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/",auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm",),
    path("password_reset_complete/",auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete",),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.index, name="index"),
    path("inscription/", views.inscription, name="inscription"),
    path("monprofil", views.monprofil, name="monprofil"),
    path("annuaire", views.annuaire, name="annuaire"),
]
