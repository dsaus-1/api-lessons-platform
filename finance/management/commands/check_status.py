from datetime import datetime, timedelta

import pytz
from django.core.management import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from config import settings


class Command(BaseCommand):
    """Создание задачи на проверку статуса платежа"""

    def handle(self, *args, **options):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=60,
            period=IntervalSchedule.SECONDS,
        )


        PeriodicTask.objects.create(
            interval=schedule,  # we created this above.
            name='Importing contacts',  # simply describes this periodic task.
            task='finance.tasks.check_status_payment',  # name of task.
            expires=datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE)) + timedelta(days=365)
        )

