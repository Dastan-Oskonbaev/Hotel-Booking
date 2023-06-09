from django.db import models
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review, Rating, RoomType
from .serializers import ReviewCreateSerializer, CreateRatingSerializer, RoomTypeDetailSerializer, \
    RoomTypeListSerializer
from .service import get_client_ip, RoomTypeFilter


class RoomTypeListView(generics.ListAPIView):
    """Вывод списка типов комнат"""
    serializer_class = RoomTypeListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RoomTypeFilter
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        room_type = RoomType.objects.filter().annotate(
            rating_user=models.Count(
                "ratings",
                filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return room_type


class RoomTypeDetailView(generics.RetrieveAPIView):
    """Вывод отеля"""
    queryset = RoomType.objects.filter()
    serializer_class = RoomTypeDetailSerializer


class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзыва к отелю"""
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()


class AddStarRatingView(generics.CreateAPIView):
    """Добавление рейтинга отелю"""
    serializer_class = CreateRatingSerializer
    queryset = Rating.objects.all()


    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))