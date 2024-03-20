import re
url = input("Введите строку: ")


def is_url(url):
    """
    На вход подаётся строка. Функция возвращает строку, если она является url-строкой,
    иначе выбрасывается исключение
    """
    pattern = re.compile(r"(http|https|ftp|smtp)://.+\.(ru|eu|cn|me|by|eg|pl|com|net|org|biz|)(/(.+)+)")
    url_check = re.fullmatch(pattern, url)
    if url_check is None:
        raise ValueError
    return url

print(is_url(url))