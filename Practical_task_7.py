def fact_gen(nunber):
    temp = 1
    for i in range(1, nunber + 1):
        temp *= i
        yield temp


number = int(input("Введите факториал числа: "))
for _ in fact_gen(number):
    print(_)
