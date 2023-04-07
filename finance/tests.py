from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Course, Lesson
from finance.models import Payment
from users.models import User
from datetime import date

class PaymentCourseTestCase(APITestCase):
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

        self.client.post(
            '/course/',
            {
                "title": "Зельеварение",
                "description": "На этом курсе не будет дурацких взмахов волшебной палочки и глупых заклинаний.",
                "students": [],
                "lessons": []
            }
        )

        Payment.objects.create(user=User.objects.filter(email='test@gmail.com').first(),
                payment_course=Course.objects.filter(title="Зельеварение").first(), payment_sum=1000,
                payment_method='cash')


    def test_payment_course_list(self):
        response = self.client.get('/finance/course/list/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{
                "user": 1,
                "payment_course": 7,
                "date_payment": str(date.today()),
                "payment_sum": 1000.0,
                "payment_method": "cash"
                }]
            )


class PaymentLessonTestCase(APITestCase):
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

        self.client.post('/lesson/create/',
                         {'title': 'Вступительный урок', 'description': 'Знакомство и общая информация о курсе',
                          'video_url': 'https://www.youtube.com/watch?v=HhHt27j3Lc0'}
                         )

        Payment.objects.create(user=User.objects.filter(email='test@gmail.com').first(),
                payment_lesson=Lesson.objects.filter(title="Вступительный урок").first(), payment_sum=100,
                payment_method='money transfer')


    def test_payment_lesson_list(self):
        response = self.client.get('/finance/lesson/list/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{
                "user": 4,
                "payment_lesson": 4,
                "date_payment": str(date.today()),
                "payment_sum": 100.0,
                "payment_method": "money transfer"
                }]
            )