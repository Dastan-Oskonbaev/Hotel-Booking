from django.db import models

from django.utils.translation import gettext_lazy as _


class Hotel(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=50,
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
        null=True,
        blank=True,
    )
    image = models.ImageField(
        _("Hotels_Image"),
        upload_to="hotels/",
        null=True,
        blank=True,
    )

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
    image = models.ImageField(
        _("Room_Image"),
        upload_to="rooms/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Room Type")
        verbose_name_plural = _("Room Types")


class Room(models.Model):
    hotel = models.ForeignKey(
        'Hotel',
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
    price = models.PositiveIntegerField(
        _("Price"),
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


class RatingStar(models.Model):
    value = models.SmallIntegerField(
        _('Value'),
        default=0
    )

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = _("Rating Star")
        verbose_name_plural = _("Rating Stars")
        ordering = ["-value"]


class Rating(models.Model):
    ip = models.CharField(
        _('IP Address'),
        max_length=15
    )
    star = models.ForeignKey(
        RatingStar,
        on_delete=models.CASCADE,
        verbose_name='star'
    )
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        verbose_name="hotel",
        related_name="ratings"
    )

    def __str__(self):
        return f"{self.star} - {self.hotel}"

    class Meta:
        verbose_name = _("Rating")
        verbose_name_plural = _("Ratings")


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(
        _("Name"),
        max_length=100
    )
    text = models.TextField(
        _("Text"),
        max_length=5000
    )
    parent = models.ForeignKey(
        'self',
        verbose_name=_("Parent"),
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name="children"
    )
    hotel = models.ForeignKey(
        Hotel,
        verbose_name="hotel",
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    def __str__(self):
        return f"{self.name} - {self.hotel}"

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')