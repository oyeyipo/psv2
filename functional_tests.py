import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_get_necessary_info_landing_page(self):
        self.browser.get("http://localhost:8000")

        self.assertIn("Oyeyipo Olawale", self.browser.title)

        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Software Engineer", header_text)

        self.fail("Finished the test")

    # def test_can_navigate_to_my_work_section(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
print("Heello")
