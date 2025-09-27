# # 2. Cho list số sau
# # numbers = [2, 5, 8, 11, 14, 17, 20]

# # In ra tất cả số trong list.

# # In ra số chẵn trong list.

# # Tính tổng tất cả số trong list.

# # In ra bảng cửu chương của từng số trong list (gợi ý: dùng for i in range(1, 11):) (bài tập nâng cao dùng for trong for, có thể làm hoặc không)

numbers = [2, 5, 8, 11, 14, 17, 20]

# #In ra tất cả số trong list.
# for i in numbers:
#     print(i)

# # In ra số chẵn trong list.
# for i in numbers:
#     if i % 2 == 0:
#         print(i)

# # Tính tổng tất cả số trong list.
# sum = 0
# for i in numbers:
#     sum += i
# print("Tổng tất cả số:", sum)

# # In ra bảng cửu chương của từng số trong list
for n in numbers:
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
        
