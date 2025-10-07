# Tính kế thừa
# Tạo một lớp cha Document có:
# __init__(self, title): Để lưu lại tiêu đề.
# Phương thức show_info(self): In ra "Tiêu đề: [tên tiêu đề]".
class Document:
    def __init__(self, title):
        self.title = title

    def show_info(self):
        print(f"Tiêu đề: {self.title}")

# Tạo lớp con Article(Document) kế thừa từ Document:
# __init__(self, title, author): Gọi __init__ của lớp cha để lưu title, và lưu thêm author.
# Viết lại (override) phương thức show_info(self) để in ra: "Bài báo: [tên tiêu đề] - Tác giả: [tên tác giả]".
class Article(Document):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def show_info(self):
        print(f"Bài báo: {self.title} - Tác giả: {self.author}")

# Tạo lớp con Email(Document) kế thừa từ Document:
# __init__(self, title, sender): Gọi __init__ của lớp cha để lưu title, và lưu thêm sender.
# Viết lại (override) phương thức show_info(self) để in ra: "Email: [tên tiêu đề] - Người gửi: [tên người gửi]".
class Email(Document):
    def __init__(self, title, sender):
        super().__init__(title)
        self.sender = sender

    def show_info(self):
        print(f"Email: {self.title} - Người gửi: {self.sender}")

email1 = Email("Request WFH", "Mai NTH")
email1.show_info()