from selenium.webdriver.remote.webelement import WebElement


class PageElement:

    def click(self):
        """click the element"""
        pass

    def double_click(self):
        pass

    def submit(self):
        pass

    def send_keys(self, keys_to_send: str):
        pass

    def clear(self):
        pass

    def is_selected(self) -> bool:
        pass

    def is_enabled(self) -> bool:
        pass

    def is_displayed(self) -> bool:
        pass

    def is_present(self) -> bool:
        pass

    def tag_name(self) -> str:
        pass

    def text(self) -> str:
        pass

    def value(self) -> str:
        pass

    def property(self, name: str) -> str:
        pass

    def attribute(self, name: str) -> str:
        pass

    def css(self, name: str) -> str:
        pass

    def size(self) -> dict:
        pass

    def location(self) -> dict:
        pass

    def webelement(self) -> WebElement:
        pass

    def screenshot_as_png(self, file):
        pass

    def upload_file(self, file: str):
        pass

    def should(self):
        pass

    def wait_until(self):
        pass

    def wait_while(self):
        pass

    def perform(self):
        pass

    def select(self):
        pass
