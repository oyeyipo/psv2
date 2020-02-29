from django.test import TestCase


class LandingPageTest(TestCase):
    def test_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'landing.html')