from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from admin_panel.models import UserTask
from django.core.files.storage import FileSystemStorage

@login_required
def user_dashboard(request):
    tasks = UserTask.objects.filter(user=request.user)
    return render(request, 'user_panel/dashboard.html', {'tasks': tasks})

@login_required
def upload_screenshot(request):
    if request.method == 'POST':
        # ✅ Use `.get()` to avoid KeyError
        screenshot = request.FILES.get('screenshot')

        if screenshot:
            fs = FileSystemStorage()
            filename = fs.save(screenshot.name, screenshot)
            return redirect('user_dashboard')  # Redirect after upload
        else:
            return render(request, 'user_panel/upload.html', {'error': 'Please select a file to upload'})

    return render(request, 'user_panel/upload.html')
