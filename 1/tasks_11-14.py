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

    first_meduim = medium_ord(lines[0])
    lines_new = []
    for word in lines:
        lines_new.append((word, (medium_ord(word) - first_meduim) ** 2))
    return lines_new


def sort_by_ascii_2(lines):
    """
    3. В порядке увеличения квадратичного отклонения между средним
    весом ASCII-кода символа в строке и максимально среднего ASCII-кода
    тройки подряд идущих символов в строке.
    """

    def medium_ord(line):
        sum_ord = sum(list(map(lambda x: ord(x), line)))
        return round(sum_ord / len(line), 4)

    def max_average_triplet(letters):
        max_average = 0
        for i in range(len(letters) - 2):
            triplet = letters[i:i + 3]
            average = sum(ord(c) for c in triplet) / 3
            max_average = max(max_average, average)
        return max_average

    return sorted(lines, key=lambda x: (medium_ord(x) - max_average_triplet(x)) ** 2)