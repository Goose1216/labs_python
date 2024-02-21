#Вариант 7
def find_sum(Num):
    Sum = 1
    for div in range(2, Num + 1):
        if Num % div == 0 and is_prime(div):
            Sum += div
    return Sum


def is_prime(Num):
    for div in range(2, Num):
        if Num % div == 0:
            return False
    return True




def count_not_even(Num):
    Cnt = 0
    while Num > 0:
        digit = Num % 10
        Cnt += 1 if digit > 3 and digit & 1 == 1 else 0
        Num //= 10
    return Cnt
