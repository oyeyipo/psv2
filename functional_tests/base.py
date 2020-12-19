import os
import time
from datetime import datetime

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    return modified_fn


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def _test_has_failed(self):
        return any(error for (method, error) in self._outcome.errors)

    def take_screenshot(self):
        filename = self._get_filename() + ".png"
        print("screenshotting to", filename)
        self.browser.get_screenshot_as_file(filename)

    def dump_html(self):
        filename = self._get_filename() + ".html"
        print("dumping page HTML to", filename)
        with open(filename, "w") as f:
            f.write(self.browser.page_source)

    def test_landing_page_header_and_lead_text(self):
        # Aduke heard about a software engineer and decides to
        # checkout his website homepage
        self.browser.get(self.live_server_url)
        # she notices the title and header mentions "Software Engineer"
        self.assertIn("Software Engineer", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Software", header_text)
