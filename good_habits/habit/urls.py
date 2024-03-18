from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.HabitCreateAPIView.as_view(), name='habit_create'),
    path('list/', views.HabitListAPIView.as_view(), name='habit_list'),
    path('public_list/', views.HabitPublicListAPIView.as_view(), name='habit_public_list'),
    path('retrieve/<int:pk>/', views.HabitRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('update/<int:pk>/', views.HabitUpdateAPIView.as_view(), name='habit_update'),
    path('delete/<int:pk>/', views.HabitDestroyAPIView.as_view(), name='habit_destroy')]
