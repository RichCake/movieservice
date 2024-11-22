from http import HTTPStatus

from django.test import TestCase


class HomepageTests(TestCase):
    # Проверка на работу страницы
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # Тест на применение верных шаблонов
    def test_template_name_correct(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, "homepage/about.html")