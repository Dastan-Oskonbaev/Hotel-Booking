from django.db import models
from django_filters import filters, FilterSet

from .models import RoomType


def get_client_ip(request):
    """Получение IP пользоваеля"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class RoomTypeFilter(FilterSet):
    class Meta:
        model = RoomType
        fields = {
            'image': ['exact'],  # Добавлено переопределение для поля 'image'
        }
        filter_overrides = {
            models.ImageField: {
                'filter_class': filters.CharFilter,  # Используйте подходящий фильтр для поля 'image'
                'extra': lambda f: {
                    'lookup_expr': 'exact',
                },
            },
        }





