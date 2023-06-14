from django.db import models
from django.db.models import Avg
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review, Rating, RoomType, Room
from .serializers import ReviewCreateSerializer, CreateRatingSerializer, RoomTypeDetailSerializer, \
    RoomTypeListSerializer, RoomSerializer
from .service import RoomTypeFilter


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


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        check_in_date = self.request.query_params.get('check_in_date')
        check_out_date = self.request.query_params.get('check_out_date')

        if check_in_date and check_out_date:
            return Room.objects.exclude(
                booking__check_out_date__gte=check_in_date,
                booking__check_in_date__lte=check_out_date
            )
        return Room.objects.all()


class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзыва к отелю"""
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticated]


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