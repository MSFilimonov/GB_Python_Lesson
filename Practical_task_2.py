def print_kwargs(**kwargs):
    return ' '.join(kwargs.values())


print(print_kwargs(name=input('Введите ваше имя: '), surname=input('Введите вашу фымилию: '),
                   year_of_birth=input('Введите ваш год рождения: '),
                   City_of_residence=input('Введите ваш город проживания :'),
                   email=input('Введите ваш email: '), telephone=input('Введите ваш телефон: ')))
