# Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров:
values_list = [6, 'список', True]
values_dict = {'a': 10, 'b': "list", 'c': False}

print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:
values_list_2 = [76, 'Распаковка']

print_params(*values_list_2, 42)
