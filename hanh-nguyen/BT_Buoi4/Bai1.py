# Cho chuỗi text = " hello world "
text = " hello world "

# Dùng len() đếm số ký tự (gồm cả khoảng trắng)
length = len(text)
print("Số ký tự của chuỗi này là:" , length)

# Dùng strip() bỏ khoảng trắng đầu và cuối + in lại chiều dài
length2 = len(text.strip())
print("Chiều dài sau khi bỏ khoảng trắng đầu và cuối là:" , length2)