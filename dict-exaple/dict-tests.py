# Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: keykey и
# valuevalue.
#
# Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу. Если
# ключа keykey нет в словаре, то нужно добавить значение в список по ключу 2 * key2∗key. Если и ключа 2 * key2∗key
# нет, то нужно добавить ключ 2 * key2∗key в словарь и сопоставить ему список из переданного элемента [value][value].

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key * 2 in d:
        d[key * 2].append(value)
    else:
        d[key * 2] = [value]


x = {}
# example
update_dictionary(x, 1, -1)
