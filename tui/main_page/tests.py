from django.test import TestCase


class TuiTest(TestCase):
    def test_about(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 301)

    def test_contacts(self):
        response = self.client.get('/contacts')
        self.assertEqual(response.status_code, 301)
