from abc import ABC, abstractmethod

#1. tạo lớp BaseElement
class BaseElement(ABC):
    def __init__(self, locator):
        self.__locator = locator
    # tạo phương thức get_locator
    def get_locator(self):
        return self.__locator
    # tạo phương thức trừu tượng click
    @abstractmethod
    def click(self):
        pass
#2. tạo lớp con Button(BaseElement) kế thừa từ BaseElement
class Button(BaseElement):
    def click(self):
        print(f"Clicking on a button with locator [{self.get_locator()}]")
#3. tạo lớp con Checkbox(BaseElement) kế thừa từ BaseElement
class Checkbox(BaseElement):
    def click(self):
        print(f"Toggling a checkbox with locator [{self.get_locator()}]")
    def is_selected():
        print(f"Checking selection status")