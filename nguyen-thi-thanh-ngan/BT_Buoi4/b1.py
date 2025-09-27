# # "1. Cho chuỗi:
#  text = "  hello world  "

# Dùng len() để đếm số ký tự (bao gồm cả khoảng trắng).
# Dùng strip() để bỏ khoảng trắng đầu và cuối, sau đó in lại chiều dài."

text = "  hello world  "
print("Độ dài chuỗi ban đầu:", len(text))

new_text = text.strip()
print("Độ dài chuỗi mới:", len(new_text))
