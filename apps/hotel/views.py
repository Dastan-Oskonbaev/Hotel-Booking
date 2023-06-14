from django.db import models
from django.db.models import Avg
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review, Rating, RoomType
from .serializers import ReviewCreateSerializer, CreateRatingSerializer, RoomTypeDetailSerializer, \
    RoomTypeListSerializer
from .service import  RoomTypeFilter


class RoomTypeListView(generics.ListAPIView):
    """Вывод списка типов комнат"""
    serializer_class = RoomTypeListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RoomTypeFilter
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = RoomType.objects.annotate(
            middle_star=Avg('ratings__star')
        )
        return queryset


class RoomTypeDetailView(generics.RetrieveAPIView):
    """Детальный вывод типа комнаты"""
    queryset = RoomType.objects.filter()
    serializer_class = RoomTypeDetailSerializer

    def get_queryset(self):
        queryset = RoomType.objects.annotate(
            middle_star=Avg('ratings__star')
        )
        return queryset

class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзыва к отелю"""
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class AddStarRatingView(generics.CreateAPIView):
    """Добавление рейтинга отелю"""
    serializer_class = CreateRatingSerializer
    queryset = Rating.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(room_type=self.get_room_type())

    def get_room_type(self):
        room_id = self.kwargs.get('room_id')
        room_type = RoomType.objects.get(id=room_id)
        return room_type