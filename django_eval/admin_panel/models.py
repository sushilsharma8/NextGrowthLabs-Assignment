from django.db import models
from django.contrib.auth.models import User

class AndroidApp(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    points = models.IntegerField()

    def __str__(self):
        return self.name

class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(AndroidApp, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.app.name}"
