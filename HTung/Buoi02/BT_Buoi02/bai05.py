# tạo set mail
emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}

#In danh sách có trong set 
#print(emails) # các giá trị giống nhau chỉ hiển thị 1.

# thêm "c@mail.com" vào danh sách
emails.add("c@mail.com")
print(emails)

#xoá "d@gmail.com"
#dùng remove -> phải có phần tử cụ thể trong set, nếu không có lúc run sẻ báo lỗi.
emails.remove("d@gmail.com")
print(emails)

#dùng discard -> không cần biết có tồn tại trong set hay không, nếu có thì sẻ xoá phần tử, không có cũng thực hiện xoá và không báo lỗi.
emails.discard("d@gmail.com")
print(emails)