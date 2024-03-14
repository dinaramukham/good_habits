from rest_framework.serializers import ValidationError


class ValidatorFeeOrHabit:
    def __init__(self, fee_some, fee_habit):
        self.field = fee_some
        self.field = fee_habit

    def __call__(self, fee_some, fee_habit):
        if fee_some != None and fee_habit.__class__ != None:
            raise ValidationError('вознаграждение либо привычка, либо предмет')


class ValidatorEasyHabit:
    def __init__(self, fee_some, fee_habit, it_easy_habit):
        self.field = fee_some
        self.field = fee_habit
        self.field = it_easy_habit

    def __call__(self, fee_some, fee_habit, it_easy_habit):
        if it_easy_habit == True and fee_habit != None:
            raise ValidationError('у приятной привычки нет вознаграждения')
        if it_easy_habit == True and fee_some != None:
            raise ValidationError('у приятной привычки нет вознаграждения')


def is_easy_habit(value):
    if value.it_easy_habit == False:
        raise ValidationError('только приятные привычки')
