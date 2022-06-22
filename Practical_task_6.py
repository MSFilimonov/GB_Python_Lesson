words = input('Введите слово из маленьких латинских букв: ')


def int_func(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]


print(int_func(words))
