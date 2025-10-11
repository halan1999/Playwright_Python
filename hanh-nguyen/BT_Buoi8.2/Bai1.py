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
        locator = self.get_locator()
        print(f"Clicking on a button with {locator}.")

class Checkbox(BaseElement):
    def click(self):
        locator = self.get_locator()
        print(f"Toggling a checkbox with {locator}")
    
    def is_selected(self):
        print("Checking selection status....")

button = Button("add_to_wishlist")
checkbox = Checkbox("marketing_subscription")

button.click()
checkbox.click()
checkbox.is_selected()