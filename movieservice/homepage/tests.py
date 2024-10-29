from django.test import SimpleTestCase


class HomepageTests(SimpleTestCase):
    # Проверка на работу страницы
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Тест на применение верных шаблонов
    def test_template_name_correct(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, "homepage/main.html")