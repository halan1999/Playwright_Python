

# Vòng lặp for được sử dụng khi bạn muốn lặp qua một chuỗi các phần tử (ví dụ: một list, tuple, string, set, dict) và thực hiện một hành động cho từng phần tử.
fruits = ["táo", "chuối", "cherry"]
# Lặp qua toàn bộ List
for fruit in fruits:
    print(fruit)

# Lặp qua một chuỗi (String)
for char in "fruits" :
    print(char)

# Lặp qua một Dictionary (Lấy Key)
fruits_name = {"name":"Lan"}
for key in fruits_name:
    print(key, "->", fruits_name[key])

# range(n) tạo ra một range của các giá trị từ `0` đến `n - 1`. 
# Kiểu `range` là một kiểu dữ liệu iterable, do đó có thể sử dụng trong vòng lặp `for`. 
# Cứ mỗi lần lặp, một giá trị từ `0` đến `n - 1` sẽ được trả về và gán cho biến `i`.

#in các số từ 0 đến 4
for i in range(5):
    print(i)

# in các số chẵn từ 2 đến 10
for c in range (2,11):
    print(c)