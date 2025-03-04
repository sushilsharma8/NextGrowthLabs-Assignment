from rest_framework import viewsets, permissions
from .models import AndroidApp, UserTask
from .serializers import AndroidAppSerializer, UserTaskSerializer

class AndroidAppViewSet(viewsets.ModelViewSet):
    queryset = AndroidApp.objects.all()
    serializer_class = AndroidAppSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserTaskViewSet(viewsets.ModelViewSet):
    queryset = UserTask.objects.all()
    serializer_class = UserTaskSerializer
    permission_classes = [permissions.IsAuthenticated]
