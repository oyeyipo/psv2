from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_do_something(self):
        self.browser.get("http://localhost:8000")

        self.assertIn("Oyeyipo Olawale", self.browser.title)
        self.fail("Finished the test")

    # def test_can_navigate_to_my_work_section(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
print("Heello")

