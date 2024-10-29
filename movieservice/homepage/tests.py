

from django.test import TestCase, Client

class PageTests(TestCase):
    def test_homepage(self):
        resp = self.client.get('/#')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('История просмотров', resp.content.decode())

    def test_admin(self):
        resp = self.client.get('/admin/', follow=True)
        self.assertEqual(resp.status_code, 200)