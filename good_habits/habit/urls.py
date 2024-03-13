from django.urls import path


from . import views


urlpatterns = [
    path('habit/create/', views.HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/list/', views.HabitListAPIView.as_view(), name='habit_list'),
    path('habit/public_list/', views.HabitPublicListAPIView.as_view(), name='habit_public_list'),
    path('habit/retrieve/<int:pk>/', views.HabitRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('habit/update/<int:pk>/', views.HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', views.HabitDestroyAPIView.as_view(), name='habit_destroy')]