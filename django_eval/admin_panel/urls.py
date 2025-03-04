from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AndroidAppViewSet, UserTaskViewSet

router = DefaultRouter()
router.register(r'apps', AndroidAppViewSet)
router.register(r'tasks', UserTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

