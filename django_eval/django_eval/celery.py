import os
from celery import Celery

# Set Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_eval.settings')

app = Celery('django_eval')

# Load Celery config from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
