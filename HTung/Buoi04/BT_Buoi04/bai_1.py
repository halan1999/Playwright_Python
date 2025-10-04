# 1. Cho chuỗi: text = "  hello world  "
# Dùng len() để đếm số ký tự (bao gồm cả khoảng trắng).
# Dùng strip() để bỏ khoảng trắng đầu và cuối, sau đó in lại chiều dài.

text = "  hello world  "

# Đếm ký tự bao gồm khoảng trắng
print("Chuỗi đã tạo:", repr(text))
print("Độ dài có khoảng cách:", len(text))

print("-"*50)

# Bỏ khoảng trắng đầu và cuối bằng strip() và in lại chiều dài
Remove_strip = text.strip()
print("Sô ký tự sau khi xoá bỏ khoảng trắng chuổi là:",len(Remove_strip))
