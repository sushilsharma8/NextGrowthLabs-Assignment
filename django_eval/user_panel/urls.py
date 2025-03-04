from django.urls import path
from .views import user_dashboard, upload_screenshot
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('upload/', upload_screenshot, name='upload_screenshot'),
    path('login/', LoginView.as_view(template_name="user_panel/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
