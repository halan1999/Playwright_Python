"""
Bài 2: Factory tạo WebDriver 
Tạo một class DriverFactory với:
    - Một phương thức @staticmethod tên là get_driver(browser_name).

    - Bên trong phương thức này, dùng if-elif-else:

        - Nếu browser_name là "chrome", in ra "Initializing Chrome Driver..." và trả về chuỗi "ChromeDriver object".

        - Nếu browser_name là "firefox", in ra "Initializing Firefox Driver..." và trả về chuỗi "FirefoxDriver object".

        - Nếu khác, raise ValueError("Browser không được hỗ trợ").

    - Hãy gọi phương thức này để tạo driver cho cả "chrome" và "edge" (để xem lỗi)
"""

class DriverFactory:

    @staticmethod
    def get_driver(browser_name):
        if browser_name == 'chrome':
            print(f"Initializing Chrome Driver...")
            return "ChromeDriver object"
        elif browser_name == 'firefox':
            print(f"Initializing Firefox Driver...")
            return "FirefoxDriver object"
        else:
            raise ValueError("Browser không được hỗ trợ")
        
chrome_drive = DriverFactory.get_driver("chrome")
edge_drive = DriverFactory.get_driver("edge")