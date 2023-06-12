from django.contrib import admin

from . import models


@admin.register(models.AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone_number',
        'email',
    )

    exclude = (
        'password',
    )
    list_display_links = ('email',)
