# scores = {6,8,9,10,4,5,6,8,9}
# #không in giá trị trùng lặp
# # ứng dung: loại bỏ các giá trị trùng lặp
# # lọc file
# print(scores)

# # thao tac dung cho Set
# students = {"Mai","Lan", "Hung", "Lan"}
# # them ban Dung
# students.add("Dung")
# # xóa bạn Hùng khỏi danh sách
# students.remove("Hung")
# # xóa bằng discard -- nếu không tồn tại keyword xóa => không báo lỗi
# students.discard("Mai")
# print(students)

# Dung set trong toan hoc
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
#cách hợp nhất dùng |
print('Tổ hợp 2 số: ',A | B)
# in ra phần giao
print(A & B)
# Hieu
print('Hiệu 2 số: ',B - A)
# ứng dụng -> xử lý tốc độ tìm kiếm
# sử dụng để compare xem menu trên ứng dụng có đủ hay dư menu
# ứng dụng sử dụng trong permitsion security nhiều
print('Loại bỏ các thông tin trùng',A ^ B)
