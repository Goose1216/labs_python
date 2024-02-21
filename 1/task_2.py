def cnt_russian_words(string):
    alph = set(x for x in "йцукенгшщзхфывапролджэячсмитьбюъ")
    cnt = 0
    for x in string:
        cnt += (x.lower() in alph)
    return cnt


print(cnt_russian_words(input()))
