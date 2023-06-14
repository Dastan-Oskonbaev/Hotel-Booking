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
    readonly_fields = (
        "name",
    )


class RatingInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description'
    )
    inlines = [ReviewInline, RatingInline]
    form = RoomTypeAdminForm


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'room_type',
        'room_number',
        'price',

    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "parent",
        "room_type",
        "id"
    )
    readonly_fields = (
        "name",
    )


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        "star",
        'room_type',
    )


admin.site.register(RatingStar)
