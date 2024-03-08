file = open('test.txt', 'r', encoding='utf-8')
read_file = file.readlines()
count_house, len_road, weight_max, max_len = (int(x) for x in read_file[0].split())
data = []


def fill_tuple():
    for text in read_file[1:]:
        num_house, weight_house = (int(x) for x in text.split())
        data.append((num_house, weight_house))


file.close()
