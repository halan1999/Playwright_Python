
 	
# 3. Viết chương trình cắt chuỗi:
# s = "Automation Testing"
 
# Lấy ra từ "Automation".
# Lấy ra từ "Testing".
# Lấy 5 ký tự đầu tiên.
# Lấy 3 ký tự cuối cùng.
s= "Automation Testing"
print(s[0:10]) #Lấy ra từ "Automation".
print(s[11:18]) #Lấy ra từ "Testing".
print(s[0:5]) #Lấy 5 ký tự đầu tiên.
print(s[-3:]) #Lấy 3 ký tự cuối cùng.
index=s.find(" ")
print(s[:index]) #Lấy ra từ "Automation".
print(s[index+1:]) #Lấy ra từ "Testing".