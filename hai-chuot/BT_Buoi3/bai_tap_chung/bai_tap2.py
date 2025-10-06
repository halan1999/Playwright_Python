# NOTE Cho list số sau
# numbers = [2, 5, 8, 11, 14, 17, 20]
# In ra tất cả số trong list.
lst_numbers = [2, 5, 8, 11, 14, 17, 20]
for number in lst_numbers:
    print(f"Index {lst_numbers.index(number)} có giá trị: {number}")

# In ra số chẵn trong list.
lst_even_number = []
for number in lst_numbers:
    if number % 2 == 0:
        lst_even_number.append(number)
print(f"\nDanh sách các số chẵn trong list: {lst_even_number}")

# Tính tổng tất cả số trong list.
print(f"\nTổng các số trong list: {sum(lst_numbers)}")

# In ra bảng cửu chương của từng số trong list (gợi ý: dùng for i in range(1, 11):) (bài tập nâng cao dùng for trong for, có thể làm hoặc không)
def print_multiplication_tables(number):
    for multiple_number in range(1, 11):        
        print(f"{number} x {multiple_number} = {number * multiple_number}")

for number in lst_numbers:
    print(f"\nBẢNG CỬU CHƯƠNG CỦA {number}")
    print_multiplication_tables(number)