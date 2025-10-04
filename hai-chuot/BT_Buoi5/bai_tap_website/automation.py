# NOTE Bài 4: Automation
# Giả lập tìm element "submit".
# Nếu không tìm thấy → in "Không tìm thấy element".
# Luôn in "Đóng trình duyệt".

def click_element(element) :
   if element == "":
        raise ValueError(f"Không tìm thấy element {element}")
   else:
       print(f"Đã click thành công đối tượng {element}")

element = str(input())
try:
    click_element(element)
except ValueError as e:
    print(e)
finally:
    print("Đóng trình duyệt!")