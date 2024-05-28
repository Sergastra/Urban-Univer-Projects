data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calc_func(structure):
    summ = 0
    for current in structure:
        if isinstance(current, list):
            summ += calc_func(current)
        if isinstance(current, tuple):
            summ += calc_func(current)
        if isinstance(current, set):
            summ += calc_func(current)
        if isinstance(current, dict):
            k, v = current.keys(), current.values()
            summ += calc_func(k)
            summ += calc_func(v)
        if isinstance(current, int):
            summ += current
        if isinstance(current, str):
            summ += len(current)
    return summ


result = calc_func(data_structure)
print(result)
