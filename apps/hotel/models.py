from django.db import models

from django.utils.translation import gettext_lazy as _


class Hotel(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=100,
        null=True,
        blank=True,
        unique=True,
    )
    address = models.CharField(
        _("Address"),
        max_length=100,
        null=True,
        blank=True,
    )
    description = models.TextField(
        _("Description"),
        max_length=500,
        blank=True,
        null=True,
    )
    image = models.ImageField

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Hotel")
        verbose_name_plural = _("Hotels")


class RoomType(models.Model):
    name = models.CharField(
        _("Room Type"),
        max_length=50,
        null=True,
        blank=True,
    )

    description = models.TextField(
        _("Description"),
        max_length=500,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Room Type")
        verbose_name_plural = _("Room Types")


class Room(models.Model):
    hotel = models.ForeignKey(
        'Hotel',
        related_name='rooms',
        verbose_name=_('Room'),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    room_type = models.ForeignKey(
        'RoomType',
        on_delete=models.CASCADE
    )
    room_number = models.CharField(
        _("Room Number"),
        max_length=100,
        null=True,
        blank=True,
        unique=True,
    )
    price = models.DecimalField(
        _("Price"),
        max_digits=8,
        decimal_places=2
    )
    is_available = models.BooleanField(
        _("Is Available"),
        default=True
    )

    def __str__(self):
        return f"Room {self.room_number} at {self.hotel.name}"

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")


