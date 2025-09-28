print("**************** Bài 1 ****************")
try:
    # Nhập số từ người dùng
    a = float(input("Nhập số a: "))

    # Thực hiện phép chia
    print(f"In bình phương của {a} = {a*a}" )

except (ValueError, ZeroDivisionError, KeyError, IndexError) as e:
    print("❌ Lỗi: ",e)

print("**************** Bài 2 ****************")
try:
    with open("data.txt", "r", encoding="uft-8") as f:
        content = f.read()
        print("Nội dung file:\n", content)
except FileExistsError:
    print("❌ File không tồn tại")
finally:
    print("Kết thúc chương trình!")

print("**************** Bài 3 ****************")
try:
    # Nhập số từ người dùng
    a = int(input("Vui lòng nhập năm sinh của bạn: "))
    b = int(2025)
    print(f"Tuổi của bạn là = {b-a}" )
except ValueError:
    print("Error: ", ValueError)
except Exception as e:
    print ("Error: ", e)
    
