# NOTE BÀI 1: Cho chuỗi:
#  text = "  hello world  "

# Dùng len() để đếm số ký tự (bao gồm cả khoảng trắng).
# Dùng strip() để bỏ khoảng trắng đầu và cuối, sau đó in lại chiều dài.

text = "  hello world  "
print(f"Độ dài của chuỗi: {len(text)}")

text = text.strip()
print(f"Độ dài của chuỗi sau khi strip: {len(text)}")