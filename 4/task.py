#Вариант 7

file = open('test.txt', 'r', encoding='utf-8')
read_file = file.readlines()
count_house, len_road, weight_max, max_len = (int(x) for x in read_file[0].split())
data = []


def fill_tuple():
    for text in read_file[1:]:
        num_house, weight_house = (int(x) for x in text.split())
        data.append((num_house, weight_house))


def first_enum():
    if max_len >= len_road // 2:
        return sum(x[1] for x in data)
    best_num_house = 0
    len_left, len_right = 0, 0
    num_house, weight_house = data[0]
    sum_weight = -(weight_house * 2)
    i = -1
    len_left_buffer = len_left
    while len_left_buffer < max_len:
        sum_weight += data[0 + i + 1]
        len_left = len_left_buffer
        len_left_buffer = (num_house - data[0 + i][0])
        if len_left_buffer < 0:
            len_left_buffer = (max_len - data[0 + i][0]) + num_house
        i -= 1
    i = 1
    len_right_buffer = len_right
    while len_right_buffer < max_len:
        sum_weight += data[0 + i - 1]
        len_right = len_right_buffer
        len_right_buffer = (data[0 + i][0] - num_house)
        if len_right_buffer < 0:
            len_right_buffer = (max_len - num_house + data[0 + i][0])
        i += 1


def other_enum():
    pass
file.close()
