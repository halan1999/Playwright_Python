# try:
#     age_input = input("Vui lòng nhập tuổi của bạn: ")
#     age = int(age_input)
#     if age < 0:
#         print("Tuổi không thể là số âm.")
#     else:
#         print(f"Bạn {age} tuổi.")
# except Exception as e:
#     # Lỗi này xảy ra khi int() không thể chuyển đổi chuỗi thành số (ví dụ: người dùng nhập "abc")
#     print("Lỗi: Dữ liệu nhập vào không phải là một con số hợp lệ.", e)


# from selenium.common.exceptions import NoSuchElementException

# # Giả sử `driver` là một đối tượng trình duyệt
# try:
#     # Cố gắng tìm và click vào pop-up quảng cáo
#     close_button = driver.find_element(By.ID, "close-popup-btn")
#     close_button.click()
#     print("Đã tìm thấy và đóng pop-up quảng cáo.")
# except NoSuchElementException:
#     # Chỉ xử lý khi element không được tìm thấy
#     print("Thông báo: Không có pop-up nào xuất hiện, tiếp tục các bước tiếp theo.")

try:
    # Nhập số từ người dùng
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))

    # Thực hiện phép chia
    result = a / b
    print("Kết quả:", result)

except (ValueError, ZeroDivisionError, KeyError, IndexError) as e:
    print("❌ Lỗi: ",e)



# try:
#     a = int(input("Nhập a = "))
#     b = int(input("Nhập b = "))

#     result = a/b
# except ValueError:
#     print("❌ Lỗi: Vui lòng nhập số hợp lệ (không phải chữ).")
# except ZeroDivisionError:
#     print("❌ Lỗi: Không thể chia cho 0.")


# try:
#     my_dict = {"name": "John"}
#     key = input("Nhập key bạn muốn truy cập: ") # Ví dụ: 'age'
#     print(my_dict[key])
# except (KeyError, IndexError) as e:
#     # Bắt cả hai lỗi: truy cập key không tồn tại trong dict, hoặc chỉ số ngoài phạm vi trong list
#     print(f"Lỗi truy cập dữ liệu: {e}")



