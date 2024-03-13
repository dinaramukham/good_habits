from django.shortcuts import render
from rest_framework import serializers, generics
from rest_framework.permissions import IsAuthenticated

from .models import Habit
from .paginators import Paginatiom
from .permission import IsOwnerPermissionsClass, IsPublicHabit
from .serializers import HabitSerializer


# Create your views here.
# ---------------------EasyHabit
class HabitCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsOwnerPermissionsClass]
    serializer_class = HabitSerializer


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsOwnerPermissionsClass]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwnerPermissionsClass]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = Paginatiom


class HabitPublicListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsOwnerPermissionsClass]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = Paginatiom

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        return Habit.objects.filter(it_public=True)


class HabitDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerPermissionsClass]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
