def print_params(a = 1, b = 'строка', c = True):
    print(a , b , c)


values_list = [True, 'str', 5]
values_dict = {'a': 2, 'b': 'hey', 'c': False}


print_params(*values_list)
print_params(**values_dict)
values_list_2 = [ True, 10]
print_params(*values_list_2, 42)