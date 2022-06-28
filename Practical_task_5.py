from functools import reduce

list = [i for i in range(100, 1001, 2)]
print("Список чётных чисел от 100 до 1000 (включая границы) : ", list)
print("Произведения всех элементов списка: ", reduce(lambda x, y: x * y, list))
