try:
    file=open("data.txt","r")
    data=file.read()
    print("nội dung file là:",data)
except (FileNotFoundError, FileExistsError,PermissionError) as e:
    print("loi:",e)
