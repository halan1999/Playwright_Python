class DriverFactory():
    def __init__(self, driver):
        self.driver = driver
    @staticmethod
    def get_driver(browser_name):
        if browser_name == "Chrome":
            print("Initializing Chrome Driver...")
            return f"ChromeDriver object"
        elif browser_name == "Firefox":
            print("Initializing Firefox Driver...")
            return f"FirefoxDriver object"
        else:
            raise ValueError("Browser không được hỗ trợ")

print(DriverFactory.get_driver("Chrome"))
print(DriverFactory.get_driver("Firefox"))
print(DriverFactory.get_driver("Edge"))
