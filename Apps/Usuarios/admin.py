from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informacion Extra', {
            'fields' : (
                'isPremium',
                'is_artist',
                'birth_date',
                'country',
                'picture',
            )
        }),
    )

admin.site.register(User, UsuarioAdmin )