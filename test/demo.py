import inspect

from selenium.webdriver.common.by import By

from pagefactory.pageobjects.page_element import PageElement
from pagefactory.pageobjects.proxy_element import Page


@Page()
class DemoPage:
    text: PageElement = (By.ID, 'text')
    disabled: PageElement = (By.ID, 'disabled')

    def v(self):
        pass


if __name__ == '__main__':
    p = DemoPage()
    v = p.text.css('222')
    p.text.clear()
    p.text()
    print(p.text)

