from unittest import TestCase

from pagefactory.browser import browsers

cfg = browsers.Configuration.of(download_directory="C:\\")


# noinspection PyMethodMayBeStatic
class BrowersTest(TestCase):

    def test_browser_type(self):
        assert cfg.browser_type == browsers.BrowserType.CHROME

    def test_headless(self):
        assert not cfg.headless

    def test_download_directory(self):
        assert cfg.download_directory.__eq__("C:\\")

    def test_page_load_time(self):
        assert cfg.page_load_time == 60

    def test_implicitly_wait_time(self):
        assert cfg.implicitly_wait_time == 0

    def test_start_chrome(self):
        chrome = browsers.Chrome(cfg)
        chrome.start()
        chrome.quit()

    def test_start_firefox(self):
        firefox = browsers.Firefox(cfg)
        firefox.start()
        firefox.quit()

    def test_start_ie(self):
        ie = browsers.InternetExplorer(cfg)
        ie.start()
        ie.quit()
