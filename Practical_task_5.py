def amount(numbers):
    numbers = numbers.split()
    b = []
    for i in numbers:
        b.append((int(i)))
    return sum(b)


sum_res = 0
while 1:
    numbers = input("Введите числа, разделенные пробелом\n"
                    "Для выхода введите символ Q \n"
                    ": ")
    if numbers.endswith('Q'):
        numbers = numbers[:-1]
        sum_res += amount(numbers)
        print("Сумма чисел: ", sum_res)
        break
    sum_res += amount(numbers)
    print("Сумма чисел: ", sum_res)
