from django.db import models
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Hotel
from .serializers import (HotelListSerializer, HotelDetailSerializer, ReviewCreateSerializer, CreateRatingSerializer)
from .service import get_client_ip, HotelFilter


class HotelListView(generics.ListAPIView):
    """Вывод списка отелей"""
    serializer_class = HotelListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HotelFilter
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        hotels = Hotel.objects.filter().annotate(
            rating_user=models.Count(
                "ratings",
                filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return hotels


class HotelDetailView(generics.RetrieveAPIView):
    """Вывод отеля"""
    queryset = Hotel.objects.filter()
    serializer_class = HotelDetailSerializer


class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзыва к отелю"""
    serializer_class = ReviewCreateSerializer


class AddStarRatingView(generics.CreateAPIView):
    """Добавление рейтинга отелю"""
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))