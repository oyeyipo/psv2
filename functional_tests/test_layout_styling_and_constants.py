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


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Aduke goes to the landing page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        # she notice the h1 text is nicely centerd
        header_textbox = self.browser.find_element_by_class_name("text-box")
        self.assertAlmostEqual(
            header_textbox.location["x"] + header_textbox.size["width"] / 2,
            512,
            delta=10,
        )
