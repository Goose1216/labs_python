from collections import deque


def open_file(name_file):
    """
    Вариант 7 Дан файл, содержащий произвольный текст. Проверить,
    правильно ли в нем расставлены круглые скобки (т.е. находится ли правее
    каждой открывающейся скобки закрывающаяся и левее закрывающейся –
    открывающаяся).
    """
    with open(name_file, "r+", encoding="UTF-8") as file:
        data = list(file.read().replace(" ", ""))
        stack = deque()
        for letter in data:
            if letter == "(":
                stack.append("*")
            elif letter == ")":
                try:
                    stack.pop()
                except IndexError:
                    return False
        if stack.count("*") == 0:
            return True
        return False

print(open_file("task2.txt"))