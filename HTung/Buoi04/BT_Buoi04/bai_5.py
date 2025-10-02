# 5. Cho list:
# fruits = ["apple", "banana", "cherry"]
# Dùng join() để nối list thành một chuỗi dạng: "apple, banana, cherry".

# Tạo fruits
fruits =["apple", "banana", "cherry"]

#Nỗi list thành 1 chuỗi
fruits_line = ", ".join(fruits)
print(fruits_line)
print("-"*50)


# ------------------------------------------------
# Kết hợp điều kiện vào
fruits_if =["banana", "cherry",2]
if fruits_if:
    print(", ".join(map(str,fruits_if)))
else:
    print("Không có phần tử nào.")