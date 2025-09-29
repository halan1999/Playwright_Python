# username = "QA_pro_123"
# length = len(username)

# print("Username là", username)
# print(f"Độ dài của tên người dùng là :  {length}")

# if 6<= length <= 20:
#     print("Tên người dùng hợp lệ.")
# else:
#     print("Tên người dùng phải có từ 6 đến 20 ký tự.") 

# error_msg = "Account not exist"
# if len(error_msg) > 0:
#     print("Message displayed")
# else:
#     print("Message not display")    

# # Ví dụ về các chuỗi hợp lệ trong code
# greeting = "Hello, World!"
# user_name = 'automation_tester_01'
# error_message = "Lỗi: Tên đăng nhập không được chứa ký tự đặc biệt."
# product_id = "SKU-12345"
# json_data = '{"id": 1, "name": "Laptop"}'
# print(user_name)

# # Chuỗi gốc không hề thay đổi
# original_text = "hello world"
# upper_text = original_text.upper()

# print("Chuỗi gốc:", original_text)      # Kết quả: hello world
# print("Chuỗi mới:", upper_text)        # Kết quả: HELLO WORLD

# user_name = "Nguyễn Thanh Lan An 123"
# print(f"Chiều dài tên {user_name} là {len(user_name)}")
# length = len(user_name)

# if( 6 <= length <= 20):
#     print("Tên người dùng hợp lệ!")
# elif( length < 6):
#     print("Tên người dùng không hợp lệ và < 6 ký tự")
# else:
#     print("Tên người dùng không hợp lệ và > 20 ký tự")
# user_name = "      nguyễn thị minh thư            "
# essay = "chào mừng bạn đến với post cast của Tâm"
# essay_cap = essay.capitalize()
# Upper_username = user_name.upper()
# lower_username = user_name.lower()
# title_username = user_name.title()
# print(f"Tên viết hoa của {user_name} là {Upper_username}")
# print(f"Tên viết thường của {user_name} là {lower_username}")
# print(f"Viết hoa chữ cái đầu {user_name} là {title_username}")

# print(f"Viết hoa chữ cái đầu tiên là {essay_cap}")

# print(user_name.strip())

# price_from_web = " \n   25,000 đ \n "
# cleaned_price = price_from_web.strip()
# expected_price = "25,000 đ"
# if cleaned_price == expected_price:
#     print(f"✅ PASSED: Giá sản phẩm hiển thị đúng là '{cleaned_price}'.")

# text = "Automation Testing"
# #       0123456789...

# # Lấy từ "Automation"
# print(text[0:10])   # Kết quả: 'Automation'
# print(text[:10])    # Cách viết tắt, tương tự như trên

# # Lấy từ "Testing"
# print(text[11:18])  # Kết quả: 'Testing'
# print(text[11:])    # Cách viết tắt

# # Lấy ký tự cuối cùng
# print(text[-1])     # Kết quả: 'g'

# # Đảo ngược chuỗi (một mẹo hay)
# print(text[::-1])   # Kết quả: 'gnitseT noitamotuA'

# text = "Nào ta cùng vui"
# lenght = len(text)
# print(f"'{text}' có {lenght} ký tự")

# print(text[:11])
# print(text[::-1]) #in chuỗi đảo ngược

# phone_number = "+84901234567"
# area_code = phone_number[:3] # Lấy 3 ký tự đầu tiên
# print(f"Lấy 3 ký tự đầu tiên của '{phone_number}'")
# print(f"=> Mã vùng: {area_code}") # Kết quả: +84

# success_message ="Đơn hàng #DH-98765 đã được tạo thành công."
# start_pos = success_message.find("#")
# order_id = success_message[start_pos : start_pos + 9]
# print(f"Trích xuất mã đơn hàng: {order_id}") # Kết quả: #DH-98765

# Lấy session ID từ URL
url = "[https://example.com/dashboard?session_id=abc123xyz&user=test](https://example.com/dashboard?session_id=abc123xyz&user=test)"
session_start = url.find("session_id=") + len("session_id=")
session_end = url.find("&", session_start)
session_id = url[session_start:session_end]
print(f"Session ID là: {session_id}") # Kết quả: abc123xyz

 