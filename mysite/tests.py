from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from mysite.views import landing_page
from django.template.loader import render_to_string


class LandingPageTest(TestCase):
    def test_landing_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "core/landing.html")

