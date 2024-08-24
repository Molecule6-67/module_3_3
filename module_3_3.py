print("Перовый пункт: ")
def print_params(a=1, b="Helloy", c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3,])
print_params(a={'a': 2, 'b': 3})

print("Второй пункт: ")
values_list = (12, "bicycle", 54.45)
print_params(*values_list)
values_dict = {'a': 5, 'b': 34, 'c': 456}
print_params(**values_dict)

print("Третий пункт: ")
values_list2 = [24.43, "Anna"]
print_params(*values_list2, 54)
