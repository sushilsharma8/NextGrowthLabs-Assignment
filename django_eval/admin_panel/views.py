from rest_framework import viewsets, permissions
from .models import AndroidApp, UserTask
from .serializers import AndroidAppSerializer, UserTaskSerializer

class AndroidAppViewSet(viewsets.ModelViewSet):
    queryset = AndroidApp.objects.all()
    serializer_class = AndroidAppSerializer
    # permission_classes = [permissions.IsAuthenticated]

class UserTaskViewSet(viewsets.ModelViewSet):
    queryset = UserTask.objects.all()
    serializer_class = UserTaskSerializer
    # permission_classes = [permissions.IsAuthenticated]

from django.shortcuts import render, redirect
from .models import AndroidApp, UserTask
from .forms import AndroidAppForm
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def admin_dashboard(request):
    apps = AndroidApp.objects.all()
    return render(request, 'admin_panel/admin_dashboard.html', {'apps': apps})

@user_passes_test(is_admin)
def add_android_app(request):
    if request.method == "POST":
        form = AndroidAppForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = AndroidAppForm()
    
    return render(request, 'admin_panel/add_app.html', {'form': form})

@user_passes_test(is_admin)
def view_uploads(request):
    uploads = UserTask.objects.all()
    return render(request, 'admin_panel/uploads.html', {'uploads': uploads})
