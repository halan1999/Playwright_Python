"""
1. Tạo một lớp trừu tượng BaseElement với:

    - __init__(self, locator) để lưu locator (private).

    - Một phương thức public get_locator() để trả về locator.

    - Một phương thức trừu tượng click().

2. Tạo lớp con Button(BaseElement) kế thừa từ BaseElement:

    - Triển khai phương thức click() bằng cách in ra: Clicking on a button with locator [locator].

3. Tạo lớp con Checkbox(BaseElement) kế thừa từ BaseElement:

    - Triển khai phương thức click() bằng cách in ra: Toggling a checkbox with locator [locator].
s
    - Thêm một phương thức riêng is_selected() in ra: Checking selection status...."""

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
        button_locator = self.__locator()
        print(f"Clicking on a button with locator {button_locator}")

class Checkbox(BaseElement):
    def click(self):
        checkbox_locator = self.__locator()
        print(f"Toggling a checkbox with locator {checkbox_locator}")

    @staticmethod
    def is_selected():
        print("Checking selection status....")

