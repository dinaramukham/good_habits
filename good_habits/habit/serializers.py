from rest_framework import serializers

from .models import Habit
from .validators import ValidatorFeeOrHabit, ValidatorEasyHabit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [ValidatorFeeOrHabit(fee_some='fee_some', fee_habit='fee_habit'),
                      ValidatorEasyHabit(fee_some='fee_some',
                                         fee_habit='fee_habit',
                                         it_easy_habit='it_easy_habit')]
