from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, TileViewSet

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('tiles', TileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
