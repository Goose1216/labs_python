import re


def find_max_number(string):
    numbers = list(map(float, re.findall(r"-?\d+\.\d+", string)))
    return max(numbers)


print(find_max_number(input()))