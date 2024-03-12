from django.core.validators import MaxValueValidator
from django.db import models

from users.models import NULLABLE

from good_habits.habit.validators import is_easy_habit


# Create your models here.
class Habit(models.Model):
    periods = [
        ('week', 'Раз в неделю'),
        ('every_day', 'Каждый день')
    ]

    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING, **NULLABLE)

    place = models.CharField(max_length=200, **NULLABLE)
    time = models.TimeField(**NULLABLE)
    action = models.CharField(max_length=200)

    fee_some = models.CharField(max_length=200, **NULLABLE, verbose_name='награда предметом')

    it_easy_habit = models.BooleanField(default=False)
    fee_habit = models.ForeignKey('Habit', on_delete=models.DO_NOTHING, **NULLABLE, validators=[is_easy_habit])

    it_public = models.BooleanField(default=True)
    period = models.CharField(choices=periods, default='every_day', max_length=20, verbose_name='периодичность')
    time_action = models.PositiveIntegerField(default=120, validators=[MaxValueValidator(120), ])
