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
