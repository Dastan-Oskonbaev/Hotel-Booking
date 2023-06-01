from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, RoomViewSet, RoomTypeViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'roomtypes', RoomTypeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
