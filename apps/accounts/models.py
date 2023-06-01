from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    phone_number = models.CharField(
        _("Phone Number"),
        max_length=20,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username
