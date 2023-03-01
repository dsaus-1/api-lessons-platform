from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User


class LessonTestCase(APITestCase):

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


    def test_lesson_create(self):

        response = self.client.post('/lesson/create/',
                                    {'title': 'Вступительный урок', 'description': 'Знакомство и общая информация о курсе',\
                      'video_url': 'https://www.youtube.com/watch?v=HhHt27j3Lc0'}
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_lesson_list(self):
        self.test_lesson_create()
        response = self.client.get('/lesson/list/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{
                'title': 'Вступительный урок',
                'preview': None,
                'description': 'Знакомство и общая информация о курсе',
                'video_url': 'https://www.youtube.com/watch?v=HhHt27j3Lc0',
                'owner_lesson': 2
            }]
        )

    def test_lesson_update(self):
        self.test_lesson_create()

        response = self.client.put('/lesson/update/3/', {'title': 'Вступительный урок', 'description': 'Обучающее видео',\
                      'video_url': 'https://www.youtube.com/watch?v=2kUEUYFbGS4'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'title': 'Вступительный урок',
                'preview': None,
                'description': 'Обучающее видео',
                'video_url': 'https://www.youtube.com/watch?v=2kUEUYFbGS4',
                'owner_lesson': 3
            }
        )

class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User(email='test@gmail.com', id=1)
        self.user.set_password('159753qwerty')
        self.user.save()

        response = self.client.post('/users/api/token/', {"email": 'test@gmail.com',
                                               "password": "159753qwerty"})

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_course_create(self):

        response = self.client.post('/course/',
                                    {
                                        "title": "Зельеварение",
                                        "description": "На этом курсе не будет дурацких взмахов волшебной палочки и глупых заклинаний.",
                                        "students": [],
                                        "lessons": []
                                    }
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_course_list(self):
        self.test_course_create()
        response = self.client.get('/course/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{
                "title": "Зельеварение",
                "preview": None,
                "description": "На этом курсе не будет дурацких взмахов волшебной палочки и глупых заклинаний.",
                "students": [],
                "lessons": [],
                "number_of_lessons": 0,
                "owner_course": 1,
                "subscription": "Unsubscribed"
                }]
        )

    def test_course_delete(self):
        self.test_course_create()
        response = self.client.delete('/course/5/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CourseSuperuserTestCase(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.user = User(email='test@gmail.com', id=1)
        self.user.set_password('159753qwerty')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()

        response = self.client.post('/users/api/token/', {"email": 'test@gmail.com',
                                                          "password": "159753qwerty"})

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_course_create(self):
        response = self.client.post('/course/',
                                    {
                                        "title": "Зельеварение",
                                        "description": "На этом курсе не будет дурацких взмахов волшебной палочки и глупых заклинаний.",
                                        "students": [],
                                        "lessons": []
                                    }
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_course_list(self):
        self.test_course_create()
        response = self.client.get('/course/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{
                "title": "Зельеварение",
                "preview": None,
                "description": "На этом курсе не будет дурацких взмахов волшебной палочки и глупых заклинаний.",
                "students": [],
                "lessons": [],
                "number_of_lessons": 0,
                "owner_course": 1,
                "subscription": "Unsubscribed"
            }]
        )

    def test_course_delete(self):
        self.test_course_create()
        response = self.client.delete('/course/2/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)






