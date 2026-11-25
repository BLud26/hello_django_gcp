from django.test import SimpleTestCase
from django.urls import reverse


# SimpleTestCase because this app has no database configured
class HelloViewTests(SimpleTestCase):

    def test_hello_page_loads(self):
        response = self.client.get(reverse('hello'))
        self.assertEqual(response.status_code, 200)

    def test_hello_page_message(self):
        response = self.client.get(reverse('hello'))
        self.assertContains(response, "What's up GCP!")
