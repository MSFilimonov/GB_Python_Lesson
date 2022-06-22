def my_func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка! Делитель не может быть нулевым.")
    except ValueError:
        print("Некорректное значение")


print(my_func(int(input("Ввелите число a: ")), int(input("Ввелите число b: "))))
