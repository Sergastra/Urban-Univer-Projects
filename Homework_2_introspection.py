def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)

    methods = [method for method in attributes if callable(getattr(obj, method))]

    module = obj.__class__.__module__

    # other_properties = {}

    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},

    # {'other_properties': other_properties}

    return info


# Интроспекция числа
number_info = introspection_info(42)
print(number_info)

# Интроспекция строки
string_info = introspection_info('Hello')
print(string_info)

# Интроспекция списка
list_info = introspection_info([1, 20, 4.0, 'word'])
print(list_info)
