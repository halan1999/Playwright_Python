try:
    file = open("data.txt","r")
    data = file.read()
    print("Noi dung trong file la:",data)
except (FileExistsError,FileNotFoundError,PermissionError) as e:
    print("Loi file: ",e)
finally:
    print("Đã kêt thuc")