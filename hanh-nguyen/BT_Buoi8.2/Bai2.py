class Browser:
    @staticmethod
    def get_driver(browser_name):
        if browser_name == "chrome":
            print("Initializing Chrome Driver...")
            return("ChromeDriver object")
        elif browser_name == "firefox":
            print("Initializing Firefox Driver...")
            return("FirefoxDriver object")
        else:
            raise ValueError("Browser không được hỗ trợ")

browser1 = "chrome"
Browser.get_driver(browser1)

browser2 = "edge"
Browser.get_driver(browser2)