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

