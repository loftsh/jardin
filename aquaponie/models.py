import datetime

import django_rq
from django.db import models

from aquaponie.tasks import ebb_rise, ebb_lower


class Ebb(models.Model):
    rising = models.DateTimeField(blank=True)
    lowering = models.DateTimeField(blank=True)

    
class ScheduledEbb(models.Model):
    rising = models.TimeField(blank=True)
    log_rising_date = models.DateField(blank=True)
    duration = models.DurationField()
    interval = models.DurationField()
    job_id = models.UUIDField()

    STATE_CHOICES = (
        ('NO', 'NONE'),
        ('QU', 'Queued'),
        ('RI', 'Rising'),
        ('LO', 'Lowering'),
    )

    state = models.CharField(max_length=2, choices=STATE_CHOICES, default='NO')

    # def set_state(self, state):
    #     states = ['NO', 'QU', 'RI', 'LO']
    #     if (states.index(state) - 1 != states.index(self.state)) and
    #        (state != 'NO'):
    #        raise ValueError("Wrong transition")

    #    sch = django_rq.get_scheduler()

    #    if state == 'RI':
    #        self.log_rising_date  = datetime.datime.now()

    #    elif state == 'LO':
    #        pass # Set lowering time for Ebb log

    #    elif state == 'QU':
    #        rising_date = datetime.datetime.now()
    #        rising_date = rising_date.replace(
    #            hour = rising.hour,
    #            minute = rising.minute,
    #            second = rising.second
    #        )
    #        if datetime.datetime.now() > rising_date:
    #            rising_date = rising_date.replace(day = rising_date.day+1)

    #         sch.enqueue_at(rising_date, self.set_state, state="RI")

    #     self.state = state
           
           
    def save(self, *args, **kwargs):
        if not self.state:
            scheduler = django_rq.get_scheduler('default')
            job_id = scheduler.enqueue_at(datetime(2020, 10, 10), ebb_rising)
            self.state = 'QU'
        super().save(*args, **kwargs)

        
class Temperature(models.Model):
    date = models.DateTimeField()
    temperature = models.FloatField()


class WaterLevel(models.Model):
    bac = models.CharField(max_length=100)
    date = models.DateTimeField()
    level = models.FloatField()
