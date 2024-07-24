def apply_all_func(int_list, *functions):
    result = {}
    f_list = functions
    for activity in f_list:
        result[activity.__name__] = activity(int_list)
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))