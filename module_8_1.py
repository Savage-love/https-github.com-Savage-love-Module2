def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)
print(add_everything_up(123.456, 'строка'))  # Выведет: 123.456строка
print(add_everything_up('яблоко', 4215))  # Выведет: яблоко4215
print(add_everything_up(123.456, 7))  # Выведет: 130.456

