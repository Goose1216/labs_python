def sort_by_subtraction(lines):
    """
    1. Отсортировать строки в порядке увеличения разницы между количеством согласных и
    количеством гласных букв в строке.
    """

    def cnt_vowels(string):
        cnt = 0
        alph = set("аиоуыэеёюя")
        for letter in string:
            if letter in alph:
                cnt += 1
        return cnt

    def cnt_consonants(string):
        cnt = 0
        alph = set("бвгджзйклмнпрстфхцчшщ")
        for letter in string:
            if letter in alph:
                cnt += 1
        return cnt

    return sorted(lines, key=lambda x: cnt_consonants(x) - cnt_vowels(x))


def sort_by_ascii(lines):
    """
    2. В порядке увеличения квадратичного отклонения среднего веса
    ASCII-кода символа строки от среднего веса ASCII-кода символа первой строки
    """

    def medium_ord(line):
        sum_ord = sum(list(map(lambda x: ord(x), line)))
        return round(sum_ord / len(line), 4)


