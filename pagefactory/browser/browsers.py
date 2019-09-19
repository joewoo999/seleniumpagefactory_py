import abc
from typing import Dict

from selenium import webdriver

from pagefactory import objects


class BrowserClassNotFoundException(Exception):
    def __init__(self, browser_type):
        super().__init__('Can not found browser class [{0}]'.format(browser_type))


class BrowserType:
    """The browsers supported"""

    FIREFOX = "firefox"
    FIREFOX_PROXY = "firefoxproxy"

    CHROME = "chrome"
    GOOGLECHROME = "googlechrome"

    IEXPLORE = "iexplore"
    IE = "ie"
    INTERNET_EXPLORER = "internet explorer"
    IEXPLORE_PROXY = "iexploreproxy"

    SAFARI = "safari"
    SAFARI_PROXY = "safariproxy"

    OPERA = "opera"
    OPERA_BLINK = "operablink"

    EDGE = "MicrosoftEdge"


__chrome__ = (BrowserType.CHROME, BrowserType.GOOGLECHROME)

__firefox__ = (BrowserType.FIREFOX, BrowserType.FIREFOX_PROXY)

__ie__ = (BrowserType.IE, BrowserType.INTERNET_EXPLORER, BrowserType.IEXPLORE)

__safari__ = (BrowserType.SAFARI, BrowserType.SAFARI_PROXY)

__opera__ = (BrowserType.OPERA, BrowserType.OPERA_BLINK)

__edge__ = (BrowserType.EDGE, "Edge")


class Configuration(Dict):

    @property
    def browser_type(self) -> str:
        return self["browser_type"]

    @browser_type.setter
    def browser_type(self, browser_type: str):
        self["browser_type"] = browser_type

    @property
    def headless(self) -> bool:
        return self["headless"]

    @headless.setter
    def headless(self, headless: bool):
        self["headless"] = headless

    @property
    def download_directory(self) -> str:
        return self["download_directory"]

    @download_directory.setter
    def download_directory(self, download_directory: str):
        self["download_directory"] = download_directory

    @property
    def page_load_time(self) -> int:
        return self["page_load_time"]

    @page_load_time.setter
    def page_load_time(self, page_load_time: int):
        self["page_load_time"] = page_load_time

    @property
    def implicitly_wait_time(self) -> int:
        return self["implicitly_wait_time"]

    @implicitly_wait_time.setter
    def implicitly_wait_time(self, implicitly_wait_time: int):
        self["implicitly_wait_time"] = implicitly_wait_time

    @staticmethod
    def of(browser_type=BrowserType.CHROME,
           headless=False,
           download_directory=None,
           page_load_time=60,
           implicitly_wait_time=0):
        conf = {"browser_type": browser_type,
                "headless": headless,
                "download_directory": download_directory,
                "page_load_time": page_load_time,
                "implicitly_wait_time": implicitly_wait_time
                }
        return Configuration(conf)


class BrowserContext:
    __driver = None

    @classmethod
    def set_driver(cls, driver: webdriver.Remote):
        cls.__driver = driver

    @classmethod
    def get_driver(cls) -> webdriver.Remote:
        if cls.__driver is not None:
            return cls.__driver
        else:
            raise ReferenceError("Webdriver instance is null, u should run 'set_driver()' first.")

    @classmethod
    def remove_all(cls):
        cls.__driver = None

    @classmethod
    def is_driver_none(cls) -> bool:  # test only
        return not objects.require_not_none(cls.__driver)


class Browser(metaclass=abc.ABCMeta):
    _types = ()

    def __init__(self, config: Configuration):
        self._driver = None
        self._config: Configuration = config

    @abc.abstractmethod
    def start(self):
        pass

    def quit(self):
        if self._driver is not None:
            self._driver.quit()
            self._driver = None

    def webdriver(self) -> webdriver.Remote:
        return self._driver

    def configuration(self) -> Configuration:
        return self._config

    @staticmethod
    def subclass(browser_type: str):
        subclasses = Browser.__subclasses__()
        for cls in subclasses:
            if browser_type in cls.__dict__.get("_types"):
                return cls

        raise BrowserClassNotFoundException(browser_type)


class Chrome(Browser):
    _types = __chrome__

    def start(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-popup-blocking")
        options.headless = self._config.headless

        if self._config.download_directory is not None:
            prefs = {"download.default_directory": self._config.download_directory,
                     "download.profile.default_content_settings.popups": 0}
            options.add_experimental_option("prefs", prefs)

        self._driver = webdriver.Chrome(options=options)


class Firefox(Browser):
    _types = __firefox__

    def start(self):
        options = webdriver.FirefoxOptions()
        options.headless = self._config.headless
        if self._config.download_directory is not None:
            options.set_preference("browser.download.useDownloadDir", True)
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.dir", self._config.download_directory)
            options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                   "application/octet-stream,application/vnd.ms-excel,application/zip,application/exe,"
                                   "application/txt")

        self._driver = webdriver.Firefox(options=options, service_log_path=None)


class InternetExplorer(Browser):
    _types = __ie__

    def start(self):
        self._driver = webdriver.Ie()


if __name__ == '__main__':
    d = webdriver.Ie()
    d.get('http://www.baidu.com')
    d.quit()
