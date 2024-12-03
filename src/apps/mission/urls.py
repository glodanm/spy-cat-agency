from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MissionViewSet, TargetViewSet



router = DefaultRouter()
router.register(r'targets', TargetViewSet, basename='target')
router.register(r'missions', MissionViewSet, basename='mission')

urlpatterns = [
    path('', include(router.urls)),
]
