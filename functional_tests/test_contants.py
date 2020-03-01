from .base import FunctionalTest


class ConstantsTest(FunctionalTest):
    def test_landing_page_header_contants(self):
        # Aduke heard about a software engineer and decides to
        # checkout his website homepage
        self.browser.get(self.live_server_url)
        # she notices the title and header mentions "Software Engineer"
        self.assertIn("Software Engineer", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Software Engineer", header_text)

        # [continued]
        self.fail("Finish the test")

