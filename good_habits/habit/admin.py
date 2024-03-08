from django.contrib import admin

from .models import EasyHabit, GoodHabit


# Register your models here.
@admin.register(EasyHabit)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'time',
                    'action', 'fee_habit', 'fee_some',
                    'is_public', 'period', 'time_action',)
    list_filter = ('user', 'place', 'time',
                    'action', 'fee_habit', 'fee_some',
                    'is_public', 'period', 'time_action',)
    search_fields = ('user', 'place', 'time',
                    'action', 'fee_habit', 'fee_some',
                    'is_public', 'period', 'time_action',)
@admin.register(GoodHabit)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('action', 'is_public',)
    list_filter = ('action', 'is_public',)
    search_fields = ('action', 'is_public',)
