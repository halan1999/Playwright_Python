#cu phap doc file la open('tên file', 'r')
try:
    file = open('data.txt', 'r')
    data = file.read()
    print('Noi dung trong file la:', data)
except (FileNotFoundError, FileExistsError, PermissionError) as e:
    print('Loi, ly do:', e)
