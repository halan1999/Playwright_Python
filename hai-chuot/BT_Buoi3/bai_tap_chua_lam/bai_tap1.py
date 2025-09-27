# NOTE 1: Kiểm trả message đăng nhập xem có nằm trong danh sách sau:
# expected_messages = [“Login succesfull”, “Welcome”]         
# actual_message = “Welcome”                                                  
# Nếu actual message nằm trong expected_messages thì in ra “Message valid” ngược lại thì in ra “Message invalid”

lst_expected_message = ["Login succesfull", "Welcome"]
actual_message = "Welcome"
# Kết quả thực tế lỗi
# actual_message = "Hello"
if actual_message in lst_expected_message:
    print("Message valid")
else:
    print("Message invalid")