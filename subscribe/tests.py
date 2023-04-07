from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class SubscribeTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User(email='test@gmail.com')
        self.user.set_password('159753qwerty')
        self.user.save()

        response = self.client.post('/users/api/token/', {"email": 'test@gmail.com',
                                                          "password": "159753qwerty"})

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')


    def test_subscribe_create(self):
        self.client.post(
            '/course/',
            {
                "title": "Зельеварение",
                "description": "На этом курсе не будет дурацких взмахов волшебной палочки и глупых заклинаний.",
                "students": [],
                "lessons": []
            }
        )
        response = self.client.post('/subscribe/subscribed/',
                                    {
                                        "student": "test@gmail.com",
                                        "course": "Зельеварение"
                                    }
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_subscribe_destroy(self):
        self.test_subscribe_create()
        response = self.client.delete('/subscribe/unsubscribed/2/',
                                    {
                                        "student": "test@gmail.com",
                                        "course": "Зельеварение"
                                    })

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

