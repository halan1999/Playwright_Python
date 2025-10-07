# Bài 1:
print("Bài 1: ")
from abc import ABC, abstractmethod

class BaseElement(ABC):
    def __init__(self, locator):
        self.__locator = locator

    def get_locator(self):
        return self.__locator

    @abstractmethod
    def click(self):
        pass

class Button(BaseElement):
    def click(self):
        print(f"Clicking on a button with locator [{self.get_locator()}]")

class Checkbox(BaseElement):
    def click(self):
        print(f"Toggling a checkbox with locator [{self.get_locator()}]")

    @staticmethod
    def is_selected():
        print("Checking selection status...")

btn = Button("save")
chk = Checkbox("checkBox")

btn.click()
chk.click()
chk.is_selected()

# Bài 2
print("\nBài 2:")

class DriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name == "chrome":
            print("Initializing Chrome Driver...")
            return "ChromeDriver object"
        elif browser_name == "firefox":
            print("Initializing Firefox Driver...")
            return "FirefoxDriver object"
        else:
            raise ValueError("Browser không được hỗ trợ")

chrome_driver = DriverFactory.get_driver("chrome")
print(chrome_driver)

edge_driver = DriverFactory.get_driver("edge")
print(edge_driver)
