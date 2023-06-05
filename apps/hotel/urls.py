from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views


urlpatterns = [
    path("hotel/", views.HotelListView.as_view()),
    path("hotel/<int:pk>/", views.HotelDetailView.as_view()),
    path("review/", views.ReviewCreateView.as_view()),
    path("rating/", views.AddStarRatingView.as_view()),
    ]