from django.contrib import admin

from apps.booking.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("room_type", "room", "guest", "checkin_date", "checkout_date", "status")
    list_per_page = 20
