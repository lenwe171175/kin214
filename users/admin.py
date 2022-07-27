from django.contrib import admin
from .models import Utilisateur
from django.contrib.auth.models import User, Group

# Register your models here.
class AdminUtilisateur(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "phone",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    )

admin.site.register(Utilisateur, AdminUtilisateur)
admin.site.unregister(Group)
admin.site.unregister(User)