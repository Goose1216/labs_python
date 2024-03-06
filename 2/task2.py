# Вариант 5

def create_files(cnt_files):
    files = {}
    for i in range(cnt_files):
        file = input().split()
        files[file[0]] = "".join(file[1:])
    return files


def check_files(cnt_operations, files):
    operations = {
        'read': "R",
        "write": "W",
        "execute": "X"
    }
    for i in range(cnt_operations):
        operation, file_name = input().split()
        if operations[operation] in files[file_name]:
            print("Access denied")
        else:
            print("OK")
