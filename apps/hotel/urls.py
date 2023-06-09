from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views


urlpatterns = [
    path("room_type/", views.RoomTypeListView.as_view()),
    path("room_type/<int:pk>/", views.RoomTypeDetailView.as_view()),
    path("review/", views.ReviewCreateView.as_view()),
    path("rating/", views.AddStarRatingView.as_view()),
    ]