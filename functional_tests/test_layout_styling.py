from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Aduke goes to the landing page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        # she notice the h1 text is nicely centerd
        header_textbox = self.browser.find_element_by_class_name("st")
        self.assertAlmostEqual(
            header_textbox.location["x"] + header_textbox.size["width"] / 2,
            512,
            delta=10,
        )
