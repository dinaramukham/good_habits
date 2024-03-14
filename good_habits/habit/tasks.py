from datetime import datetime

from celery import shared_task

from .models import Habit


@shared_task
def my_task():
    every_habits = Habit.objects.filter(it_easy_habit=False, period='every day')
    habit_times=[]
    for habit in every_habits:
        habit_time= habit.time
        habit_place = habit.place
        habit_action = habit.action
