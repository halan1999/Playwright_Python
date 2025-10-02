# tạo danh sách (list) chứa 2 chuỗi 
expected_messages = ["Login succesful", "Welcome"]

#Tạo biến rồi gán giá trị
actual_message = "Welcome" 

# Dùng toán tử in để kiểm tra giá trị của actual message nằm trong expected_messages
if actual_message in expected_messages:
    print("Message valid")
else: 
    print("Message invalid")