# Дана строка. Необходимо найти наибольшее количество идущих
# подряд цифр.


def cnt_numbers(string):
    cnt_num = 0
    cnt_num_max = 0
    for letter in string:
        if letter in "0123456789":
            cnt_num += 1
        else:
            cnt_num_max = max(cnt_num_max, cnt_num)
            cnt_num = 0
    return cnt_num_max


print(cnt_numbers(input()))