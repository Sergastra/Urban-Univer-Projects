# функция с произвольным числом параметров разного типа
def test(*params, **value):
    print(type(params))
    print(params)
    print(type(value))
    print(value)


test(1, 'Anton', True, [5, 6, 7], name="Daniel")


# факториал от числа n
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Введите число:"))
print("Факториал числа равен:")
print(factorial(n))
