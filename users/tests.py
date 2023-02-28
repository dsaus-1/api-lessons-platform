from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User(email='test@gmail.com')
        self.user.set_password('159753qwerty')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()

        response = self.client.post('/users/api/token/', {"email": 'test@gmail.com',
                                               "password": "159753qwerty"})

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_user_create(self):
        response = self.client.post('/users/',
                                    {"email": "test123@gmail.com",
                                     "password": "159753qwerty"}
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_list(self):
        response = self.client.get('/users/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "email": "test@gmail.com",
                    "phone": None,
                    "city": None,
                    "avatar": None
                }
            ]
            )

    def test_user_update(self):
        response = self.client.put('/users/6/', {"email": "test@gmail.com",
                                                 "password": "159753qwerty",
                                                 "phone": 132132132})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
                {
                    "email": "test@gmail.com",
                    "phone": "132132132",
                    "city": None,
                    "avatar": None
                }
        )

    def test_user_detail(self):
        response = self.client.get('/users/4/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "email": "test@gmail.com",
                "phone": None,
                "city": None,
                "avatar": None
            }
        )

    def test_user_delete(self):
        response = self.client.delete('/users/3/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


