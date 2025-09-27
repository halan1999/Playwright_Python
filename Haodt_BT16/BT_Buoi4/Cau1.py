text = "  hello world  "
# Dùng len() để đếm số ký tự (bao gồm cả khoảng trắng).
length = len(text)
print(f"Độ dài kể cả khoảng trắng:",length)

# Dùng strip() để bỏ khoảng trắng đầu và cuối, sau đó in lại chiều dài.
text=text.strip()
length = len(text)
print(f'Độ dài sau khi bỏ khoảng trắng:',length)
print(f'Giá trị text sau khi bỏ khoảng trắng:',text)
