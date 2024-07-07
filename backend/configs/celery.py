# celery
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')
app = Celery('configs')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'update_currency': {
        'task': 'apps.cars.tasks.get_exchange_rates',
        'schedule': crontab(minute='0', hour='0'),
    }
}
