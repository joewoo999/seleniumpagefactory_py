from unittest import TestCase

from pagefactory.browser.browsers import Configuration, BrowserContext
from pagefactory.browser.browser_factory import BrowserFactory

cfg = Configuration.of(browser_type="ie")


# noinspection PyMethodMayBeStatic
class BrowerFactoryTest(TestCase):
    def test_set_up(self):
        BrowserFactory.set_up(cfg)
        assert BrowserContext.get_driver() is not None

    def test_tear_down(self):
        BrowserFactory.tear_down()
        with self.assertRaises(ReferenceError) as info:
            BrowserContext.get_driver()

