from django.core.validators import MaxValueValidator
from django.db import models

from users.models import NULLABLE


# Create your models here.
class GoodHabit(models.Model):
    periods = [
        ('week', 'Раз в неделю'),
        ('every_day', 'Каждый день')
    ]

    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING, **NULLABLE)

    place = models.CharField(max_length=200, **NULLABLE)
    time = models.TimeField(**NULLABLE)
    action = models.CharField(max_length=200)

    fee_habit = models.OneToOneField('EasyHabit', on_delete=models.DO_NOTHING, **NULLABLE,
                                     verbose_name='награда привычкой')
    fee_some = models.CharField(max_length=200, **NULLABLE, verbose_name='награда предметом')

    is_public = models.BooleanField(default=True)
    period = models.CharField(choices=periods, default='every_day', max_length=20, verbose_name='периодичность')
    time_action = models.PositiveIntegerField(default=120, validators=[MaxValueValidator(120), ])


class EasyHabit(models.Model):
    action = models.CharField(max_length=200)
    is_public = models.BooleanField(default=True)
