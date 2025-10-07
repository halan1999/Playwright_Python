from abc  import ABC, abstractmethod
class BaseElement:
    def __init__(self, locator):
        self.locator = locator
    def get_locator(self):
        return self.locator
    @abstractmethod
    def click(self):
        pass
class Buttton(BaseElement):
    def __init__(self, locator):
        super().__init__(locator)
    def click(self):
        print(f"Clicking on a button with locator{super().get_locator()}")

class CheckBox(BaseElement):
    def __init__(self, locator):
        super().__init__(locator)
    
    def click(self):
        print(f"Toggling a checkbox with locator {super().get_locator()}")
    def is_selected(self):
        print("Checking selection status....")

btnLogin = Buttton("XpathBtnLogin")
chkChoose = CheckBox("XpathChekChoose")

btnLogin.click()
chkChoose.click()