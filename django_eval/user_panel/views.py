from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def upload_screenshot(request):
    if request.method == 'POST' and request.FILES['screenshot']:
        screenshot = request.FILES['screenshot']
        fs = FileSystemStorage()
        filename = fs.save(screenshot.name, screenshot)
        return render(request, 'user_panel/upload.html', {'filename': filename})
    return render(request, 'user_panel/upload.html')
