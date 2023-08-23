import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
app = Celery('mysite', broker='redis://127.0.0.1/1')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()