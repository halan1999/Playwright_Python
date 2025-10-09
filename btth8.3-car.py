#Thiết kế Xe hơi: 
# Viết một class Car với hàm __init__ nhận vào 2 tham số là brand (hãng xe) và model. 
# Bên trong __init__, hãy gán chúng cho các thuộc tính self.brand và self.model. 
# Sau đó, tạo ra 2 đối tượng xe hơi khác nhau và in ra thông tin của chúng.

class Car:
    def __init__(self,branch,model):
        self.branch = branch
        self.model = model

cp1 = Car("Kia","K9")
cp2 = Car("Mercedes","G63")

print("Hãng xe",cp1.branch)
print("Đời xe",cp2.model)

