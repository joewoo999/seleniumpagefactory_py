from selenium.webdriver.remote.webelement import WebElement
from pagefactory.pageobjects.page_element import PageElement


class PageElementLocator:

    def __init__(self, search_context, locator: tuple):
        self.search_context = search_context
        self.locator = locator
        self.by, self.value = locator

    def __repr__(self):
        return repr(self.locator)

    def find_element(self) -> WebElement:
        return self.search_context.find_element(self.by, self.value)

    def find_elements(self) -> list:
        return self.search_context.find_elements(self.by, self.value)


class PageElementHandler:

    def __init__(self, locator: PageElementLocator, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.locator = locator

    def __repr__(self):
        return repr(self.locator)

    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        return self


class ProxyObject:

    def __init__(self, handler):
        self.handler = handler

    def __repr__(self):
        return repr(self.handler)

    def __call__(self, *args, **kwargs):
        return self.handler(self.method, *args, **kwargs)

    def __getattr__(self, item):
        self.method = item
        return self


class Page:

    def __init__(self, po_cls=PageElement, driver=None):
        self.po_cls = po_cls
        self.driver = driver

    def __call__(self, page_cls):
        for f_name, f_cls in getattr(page_cls, '__annotations__', {}).items():
            if issubclass(f_cls, self.po_cls):
                field = getattr(page_cls, f_name)
                handler = PageElementHandler(PageElementLocator(self.driver, field))
                setattr(page_cls, f_name, ProxyObject(handler))
        return page_cls
