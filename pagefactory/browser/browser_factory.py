from pagefactory.browser.browsers import Browser, Configuration, BrowserContext


class BrowserFactory:
    __bwr: Browser = None

    @classmethod
    def set_up(cls, config: Configuration):
        browser_class = Browser.subclass(config.browser_type)
        cls.__bwr = browser_class(config)
        cls.__bwr.start()
        BrowserContext.set_driver(cls.__bwr.webdriver())

    @classmethod
    def tear_down(cls):
        if cls.__bwr is not None:
            cls.__bwr.quit()
            del cls.__bwr
            BrowserContext.remove_all()
