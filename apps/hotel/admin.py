from django.contrib import admin

from apps.hotel.models import Hotel, Room, RoomType


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = '__all__'


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = '__all__'


@admin.site.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = '__all__'
