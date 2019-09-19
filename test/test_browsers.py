import warnings
from unittest import TestCase

from pagefactory.browser import browsers


# noinspection PyMethodMayBeStatic
class BrowersTest(TestCase):

    def setUp(self) -> None:
        self.cfg = browsers.Configuration.of(headless=True, download_directory="C:\\")
        warnings.simplefilter("ignore", ResourceWarning)

    def test_browser_type(self):
        assert self.cfg.browser_type == browsers.BrowserType.CHROME

    def test_headless(self):
        self.assertTrue(self.cfg.headless)

    def test_download_directory(self):
        self.assertEqual(self.cfg.download_directory, "C:\\")

    def test_page_load_time(self):
        assert self.cfg.page_load_time == 60

    def test_implicitly_wait_time(self):
        assert self.cfg.implicitly_wait_time == 0

    def test_start_chrome(self):
        chrome = browsers.Chrome(self.cfg)
        chrome.start()
        chrome.quit()

    def test_start_ie(self):
        ie = browsers.InternetExplorer(self.cfg)
        ie.start()
        ie.quit()

    def test_start_firefox(self):
        firefox = browsers.Firefox(self.cfg)
        firefox.start()
        firefox.quit()
