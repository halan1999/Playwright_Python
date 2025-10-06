class DriverFactory:    
    @staticmethod
    def get_driver(driver):
        if driver.lower() == "chrome":
            print("Initializing Chrome Driver...")
            return "ChromeDriver object"
        elif driver.lower() == "firefox":
            print("Initializing Firefox Driver...")
            return "FirefoxDriver object"
        else:
            raise ValueError("Browser không được hỗ trợ")

try:
    print(DriverFactory.get_driver("CHROME"))
    print()
    print(DriverFactory.get_driver("Firefox"))
    print()
    print(DriverFactory.get_driver("EDGE"))
except ValueError as e:
    print(e)