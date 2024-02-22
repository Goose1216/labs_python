import re


def find_all_dates(string):
    moths = [
        'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
    ]
    moths_for_pattern = "|".join(moths)
    answer_group = re.findall(r"([0-2]\d|3[0-1]) (" + moths_for_pattern + ") (\d{4})", string)
    return tuple(map(lambda x: ' '.join(x), answer_group))


print(*find_all_dates(input()), sep=', ')
