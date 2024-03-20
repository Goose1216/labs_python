# Вариант 7
import math

file = open('B.txt', 'r', encoding='utf-8')
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
    ind_house_left, ind_house_right = count_house - 1, 1
    num_house, weight_house = data[0]
    cnt_packets = math.ceil(weight_house / weight_max)
    i = -2
    len_left = 0
    len_left_next = (len_road - data[-1][0] + num_house)
    while len_left < max_len:
        ind_house_left -= 1
        len_left = len_left_next
        cnt_packets += math.ceil(data[0 + i + 1][1] / weight_max)
        len_left_next = (len_road - data[0 + i][0]) + num_house
        i -= 1
    i = 2
    len_right_last = (data[1][0] - num_house)
    len_right = 0
    while len_right < max_len:
        ind_house_right += 1
        len_right = len_right_last
        cnt_packets += math.ceil(data[0 + i - 1][1] / weight_max)
        len_right_last = data[0 + i][0] - num_house
        i += 1
    return ind_house_left, ind_house_right, cnt_packets


def enum():
    try:
        ind_house_left_last, ind_house_right_last, cnt_packets_first = first_enum()
    except:
        return first_enum()
    cnt_packets_min = cnt_packets_first
    cnt_packets_last = cnt_packets_first
    num_house_last = data[0][0]
    num_house_left_last = data[ind_house_left_last][0]
    cnt_packets_left_last = math.ceil(data[ind_house_left_last][1] / weight_max)
    num_house_right_last = data[ind_house_right_last][0]
    cnt_packets_right_last = math.ceil(data[ind_house_right_last][1] / weight_max)
    for ind_house_new in range(1, len(data)):
        ind_house_left_new = (ind_house_left_last + 1) % count_house
        cnt_packets_left_new = math.ceil(data[ind_house_left_new][1] / weight_max)
        ind_house_right_new = (num_house_right_last + 1) % count_house
        cnt_packets_right_new = math.ceil(data[ind_house_left_new][1] / weight_max)
        cnt_packets_new = cnt_packets_last - cnt_packets_left_last + cnt_packets_right_new
        cnt_packets_min = min(cnt_packets_new, cnt_packets_min)
    return cnt_packets_min


fill_tuple()
print(enum())
file.close()
