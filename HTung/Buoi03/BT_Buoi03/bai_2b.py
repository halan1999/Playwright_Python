# Cho list số sau
# numbers = [2, 5, 8, 11, 14, 17, 20]
# In ra tất cả số trong list.
# In ra số chẵn trong list.
# Tính tổng tất cả số trong list.
# In ra bảng cửu chương của từng số trong list (gợi ý: dùng for i in range(1, 11):) (bài tập nâng cao dùng for trong for, có thể làm hoặc không)

# Tạo danh sách
numbers = [2, 5, 8, 11, 14, 17, 20]
# in ra tất cả các số có trong list đã tạo
print("\nCác số có trong danh sách là:\n",numbers)

# In ra số chẵn trong list.
for i in numbers :
    if i % 2 == 0:
        print(f"\nSố {i} là số chẵn")

# Tính tổng tất cả số trong list.
print("\nTổng tất cả các số có trong List là: ",sum(numbers))


#print("\nBảng cửu chương 3: ")
#for i in range(1,11): #đặt biến i để thực hiện gán giá trị
#    print(f"3 x {i} = { 3 * i }") 

for i in numbers : # đăt i để duyệt toàn bộ phần tử có trong numbser
    print(f"\nBảng cửu chương {i}:") # in ra phần từ i khi thực hiện duyệt
    for f in range(1,11): #đặt biến f để thực hiện gán giá trị và thực hiện từ 1 đến 11 -1
        print(f"{i} x {f} = { i * f }") 