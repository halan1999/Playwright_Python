#  Cho chuỗi  text = "  hello world  ". Dùng len để đếm số ký tự trong chuỗi textm bao gồm cả khoản trắng ở đầu và cuối chuỗi.
text = "  hello world  "
print(len(text))  # Output: 15
#  Dùng hàm strip() để loại bỏ khoảng trắng ở đầu và cuối chuỗi, sau đó in lại chiều dài
print(len(text.strip()))  # Output: 11