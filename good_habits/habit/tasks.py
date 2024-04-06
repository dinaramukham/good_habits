from datetime import datetime

from celery import shared_task

from .models import Habit
from .services import MyBot


@shared_task
def every_day_task():
    every_habits = Habit.objects.filter(it_easy_habit=False, period='every day')
    my_bot = MyBot()
    for habit in every_habits:
        habit_time = habit.time
        habit_place = habit.place
        habit_action = habit.action
        message = f'Я буду {habit_action} в {habit_time} в {habit_place}'
        my_bot.send_message(message)


@shared_task
def every_week_task():
    every_habits = Habit.objects.filter(it_easy_habit=False, period='week')
    my_bot = MyBot()
    for habit in every_habits:
        habit_time = habit.time
        habit_place = habit.place
        habit_action = habit.action
        message = f'Я буду {habit_action} в {habit_time} в {habit_place}'
        my_bot.send_message(message)
