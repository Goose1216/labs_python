def is_palindrome(string):
    alph = set('abcdefghijklmnopqrstuvwxyz')
    word = ""
    word_turned = ""
    for letter in string:
        if letter in alph:
            word += letter
            word_turned = letter + word_turned
    return word_turned == word and word != ""

print(is_palindrome(input()))
