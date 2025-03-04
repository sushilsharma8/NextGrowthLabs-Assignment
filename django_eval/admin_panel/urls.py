from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AndroidAppViewSet, UserTaskViewSet, admin_dashboard, add_android_app, view_uploads

router = DefaultRouter()
router.register(r'apps', AndroidAppViewSet)
router.register(r'tasks', UserTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('add-app/', add_android_app, name='add_android_app'),
    path('view-uploads/', view_uploads, name='view_uploads'),
]

