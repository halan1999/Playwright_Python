# try:
#     age_input = input("Bạn hãy nhập tuổi:")
#     age = int(age_input)
#     if(age > 0):
#         print("Tuoi của bạn là: ", age)
# except ValueError:
#         print("Kiểu dữ liệu không hợp lệ")
# except ValueError as e:
#     print("Lỗi hệ thống:",e)

#-----------------------------------------------------
try:
    input_a = input("Nhập giá trị của a: ")
    input_b = input("Nhập giá trị của b: ")
    int_a = int(input_a)
    int_b = int(input_b)
    
    # Gán kết quả
    result = int_a/int_b

except ValueError as e:
    print("Kiểu dữ liệu không hợp lệ:",e)
except ZeroDivisionError:
    print("Không thể chia hết cho 0")
else:
    print(f"Kết quả là {result}")
