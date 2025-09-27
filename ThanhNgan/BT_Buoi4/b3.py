# "3. Viết chương trình cắt chuỗi:
# s = ""Automation Testing""
 
# Lấy ra từ ""Automation"".
# Lấy ra từ ""Testing"".
# Lấy 5 ký tự đầu tiên.
# Lấy 3 ký tự cuối cùng."

s = "Automation Testing"
print("* Lấy ra từ 'Automation':", s[:s.find(" ")])
print("* Lấy ra từ 'Testing':", s[s.find(" ") + 1:])
print("* Lấy 5 ký tự đầu tiên:", s[0:5])
print("* Lấy 3 ký tự cuối cùng:", s[len(s) - 3:])
