def sort_by_subtraction(lines):
    """
    Отсортировать строки в порядке увеличения разницы между количеством согласных и
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


