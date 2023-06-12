from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import related
from django.utils.translation import gettext_lazy as _


from apps.hotel.models import RoomType, Room

User = get_user_model()
STATUS_CHOICES = (
    (0, 'Pending'),
    (1, 'Approved'),
    (2, 'Rejected'),
)


class Booking(models.Model):
    guest = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        RoomType,
        on_delete=models.CASCADE,

    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='booking',
        verbose_name='Room'
    )
    num_of_guest = models.PositiveIntegerField(
        _('Number of guest'),
        default=0
    )
    checkin_date = models.DateField(
        _('Checkin date'),
        null=True,
        blank=True
    )
    checkout_date = models.DateField(
        _('Checkout date'),
        null=True,
        blank=True
    )
    is_checkout = models.BooleanField(
        _('Is_Checkout'),
        default=True
    )
    status = models.IntegerField(
        _('Status'),
        choices=STATUS_CHOICES,
        default=0
    )

    def __str__(self) -> str:
        return self.guest.username if self.guest else "Гость не зарегистрирован"

    def hotel_name(self):
        return self.hotel.name

    def charge(self) -> float:
        return (self.checkout_date - self.checkin_date + timedelta(1)).days * self.room.price
