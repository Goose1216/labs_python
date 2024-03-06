# Вариант 5

def create_files(cnt_files):
    files = {}
    for i in range(cnt_files):
        file = input().split()
        files[file[0]] = "".join(file[1:])
    return files

