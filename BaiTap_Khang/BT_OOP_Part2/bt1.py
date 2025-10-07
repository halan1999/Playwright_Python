# Tạo một lớp trừu tượng BaseElement với:
# __init__(self, locator) để lưu locator (private).
# Một phương thức public get_locator() để trả về locator.
# Một phương thức trừu tượng click().
# Tạo lớp con Button(BaseElement) kế thừa từ BaseElement:
# Triển khai phương thức click() bằng cách in ra: Clicking on a button with locator [locator].
# Tạo lớp con Checkbox(BaseElement) kế thừa từ BaseElement:
# Triển khai phương thức click() bằng cách in ra: Toggling a checkbox with locator [locator].
# Thêm một phương thức riêng is_selected() in ra: Checking selection status....

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

class CheckBox(BaseElement):
    def click(self):
        print(f"Toggling a checkbox with locator [{self.get_locator()}]")
    def is_selected(self):
        print("Checking selection status...")

