from copy import deepcopy


def cycle_shift(array):
    """
    1. Дан целочисленный массив. Необходимо осуществить циклический
    сдвиг элементов массива вправо на две позиции.
    """
    len_array = len(array)
    array_new = deepcopy(array)
    for i in range(len_array):
        array_new[(i + 2) % (len_array)] = array[i]
    return array_new


def cycle_shift_2(array):
    """
    2. Дан целочисленный массив. Необходимо осуществить циклический
    сдвиг элементов массива вправо на одну позицию.
    """
    len_array = len(array)
    array_new = deepcopy(array)
    for i in range(len_array):
        array_new[(i + 1) % (len_array)] = array[i]
    return array_new


def cnt_even_num(array):
    """
    3. Дан целочисленный массив. Найти количество чётных элементов.
    """
    cnt_even = 0
    for num in array:
        if isinstance(num, int) and num & 1 == 0:
            cnt_even += 1
    return cnt_even


def cnt_even_min_num(array):
    """
    Дан целочисленный массив. Необходимо найти количество минимальных элементов.
    """
    min_num = float("inf")
    for num in array:
        if isinstance(num, int):
            min_num = min(num, min_num)
    cnt = 0
    for num in array:
        if num == min_num:
            cnt += 1
    return cnt

