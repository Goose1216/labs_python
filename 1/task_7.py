import re


def find_max_number(string):

    def convert_to_float(string_rational):
        num1, num2 = string_rational.split("/")
        return round(int(num1) / int(num2), 5)

    numbers = list(map(convert_to_float, re.findall(r"-?\d+/\d+", string)))
    return max(numbers)


print(find_max_number(input()))