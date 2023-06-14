from rest_framework import serializers

from .models import Review, Rating, RoomType


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class RoomTypeListSerializer(serializers.ModelSerializer):
    """Список отелей"""
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = RoomType
        fields = ("id", "name", "rating_user", "middle_star")


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыво"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("id", "name", "text", "children")


class RoomTypeDetailSerializer(serializers.ModelSerializer):
    """Детальный вид отеля"""
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.FloatField(source='middle_star')

    class Meta:
        model = RoomType
        fields = "__all__"


class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""
    class Meta:
        model = Rating
        fields = ("star", "room_type")

    def create(self, validated_data):
        user = self.context['request'].user
        rating, _ = Rating.objects.update_or_create(
            user=user,
            room_type=validated_data.get('room_type', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating
