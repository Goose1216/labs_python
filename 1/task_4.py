import re
# Найти в тексте даты формата «день.месяц.год».

def find_dates(string):
    answer_group = re.findall(r"([0-2]\d|3[0-1])\.(0\d|1[0-2])\.(\d{4})", string)
    return tuple(map(lambda x: '.'.join(x), answer_group))


print(*find_dates(input()), sep=', ')
