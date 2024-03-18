from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from .models import Habit
from .users.models import User


# Create your tests here.
class HabitTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='testuser@gmail.ru', is_superuser=True, is_staff=True)
        self.user.set_password('testtesttest')

        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        data = {'user': self.user, 'action': 'test'}
        response = self.client.post('habit/create/', data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_list_habit(self):
        response = self.client.get('habit/list/')
        self.assertEquals(response.status_code, status.HTTP_200_OK, )

    def test_destroy_habit(self):
        course = Habit.objects.create(user=self.user, title='test course', content='test content')
        response = self.client.delete(f'habit/delete/{course.id}/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_habit(self):
        course = Habit.objects.create(user=self.user, title='test course', content='test content')
        new_title = "new test"
        response = self.client.patch(f'/habit/update/{course.id}/', data={"place": new_title}, )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_public_list_habit(self):
        response = self.client.get('habit/public_list/')
        self.assertEquals(response.status_code, status.HTTP_200_OK, )
