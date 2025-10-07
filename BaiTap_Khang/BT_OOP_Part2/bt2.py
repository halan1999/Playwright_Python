# Một phương thức @staticmethod tên là get_driver(browser_name).
# Bên trong phương thức này, dùng if-elif-else:
# Nếu browser_name là "chrome", in ra "Initializing Chrome Driver..." và trả về chuỗi "ChromeDriver object".
# Nếu browser_name là "firefox", in ra "Initializing Firefox Driver..." và trả về chuỗi "FirefoxDriver object".
# Nếu khác, raise ValueError("Browser không được hỗ trợ").
# Hãy gọi phương thức này để tạo driver cho cả "chrome" và "edge" (để xem lỗi).