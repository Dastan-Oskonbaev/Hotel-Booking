from django import forms
from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from apps.hotel.models import Hotel, Room, RoomType, Review, Rating, RatingStar


class HotelAdminForm(forms.ModelForm):
    description = forms.CharField(
        label="Description",
        widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = Hotel
        fields = '__all__'


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'description',
    )
    inlines = [ReviewInline]
    form = HotelAdminForm



@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'room_type',
        'room_number',
        'price',

    )


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description'
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "hotel", "id")
    readonly_fields = ("name", "email")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "hotel", "ip")

admin.site.register(RatingStar)
