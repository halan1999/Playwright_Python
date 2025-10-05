# 3. Viết chương trình cắt chuỗi:
# s = "Automation Testing"
 
# Lấy ra từ "Automation".
# Lấy ra từ "Testing".
# Lấy 5 ký tự đầu tiên.
# Lấy 3 ký tự cuối cùng.

text_List= " Automation Testing "
text_List = text_List.strip()
# Lấy ra từ "Automation".
print("Lấy ra từ:",text_List[0:10])
print("-"*50)

# Lấy ra từ "Testing"
print("Lấy ra từ:",text_List[11:18])
print("-"*50)

# Lấy 5 ký tự đầu tiên.
print("Lấy 5 ký tự đầu tiên:",text_List[0:5])
print("-"*50)

# Lấy 3 ký tự cuối cùng
print("Lấy 3 ký tự cuối cùng:",text_List[-3:])
print("-"*50)