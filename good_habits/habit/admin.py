from django.contrib import admin

from .models import Habit


# Register your models here.
@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'time',
                    'action', 'fee_some', 'it_easy_habit',
                    'fee_habit', 'it_public', 'period', 'time_action',)
    list_filter = ('user', 'place', 'time',
                    'action', 'fee_some', 'it_easy_habit',
                    'fee_habit', 'it_public', 'period', 'time_action',)
    search_fields = ('user', 'place', 'time',
                    'action', 'fee_some', 'it_easy_habit',
                    'fee_habit', 'it_public', 'period', 'time_action',)



