# Trích xuất tên người dùng: Cho một địa chỉ email user_email = "automation.tester01@g-mail.com". 
# Viết code để lấy ra phần tên người dùng (username) là "automation.tester01".
user_email = "automation.tester01@g-mail.com"
# username = user_email.split('@')[0]
# print(username)
index=user_email.find("@")
username=user_email[0:index]
print(username)