
from django.db import models
from django.utils.translation import gettext_lazy as _


class AuthUser(models.Model):
    first_name = models.CharField(
        _('First name'),
        max_length=50,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        _('Last name'),
        max_length=50,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        _('Email'),
        max_length=255,
        unique=True,
    )
    phone_number = models.CharField(
        _('Phone Number'),
        max_length=30,
        unique=True,
    )


    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return f" {self.first_name} {self.last_name}"
