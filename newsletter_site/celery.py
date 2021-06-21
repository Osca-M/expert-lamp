import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsletter_site.settings')

app = Celery('newsletter_site')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
