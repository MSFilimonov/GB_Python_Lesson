def int_func(words):
    first_letter_small = words[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + words[1:]


source_words = input('Введите слова из маленьких латинских букв: ').split()
result = []
for words in source_words:
    result.append(int_func(words))
print(' '.join(result))
