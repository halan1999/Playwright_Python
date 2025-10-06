from abc import ABC, abstractmethod

class BaseElement:
    def __init__(self, locator):
        self.__locator = locator

    def get_locator(self):
        return self.__locator
    
    @abstractmethod
    def click(self):
        pass

class Button(BaseElement):
    def __init__(self, locator):
        super().__init__(locator)

    def click(self):
        print(f"Clicking on a button with locator {super().get_locator()}.")

class Checkbox(BaseElement):
    def __init__(self, locator):
        super().__init__(locator)
    
    def click(self):
        print(f"Toggling a checkbox with locator {super().get_locator()}.")

    def is_selected(self):
        print("Checking selection status...")


button_login = Button("XPath Button Login")
checkbox_send_email = Checkbox("Xpath Send Email")

button_login.click()
checkbox_send_email.click()
checkbox_send_email.is_selected()