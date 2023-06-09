from django import forms
from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from apps.hotel.models import Room, RoomType, Review, Rating, RatingStar


class RoomTypeAdminForm(forms.ModelForm):
    description = forms.CharField(
        label="Description",
        widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = RoomType
        fields = '__all__'


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [ReviewInline]
    form = RoomTypeAdminForm


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'room_type',
        'room_number',
        'price',

    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "room_type", "id")
    readonly_fields = ("name", "email")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", 'room_type', "ip")


admin.site.register(RatingStar)
