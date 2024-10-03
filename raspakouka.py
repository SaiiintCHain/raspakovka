def print_params(a = 3, b = 6 ,c = 5):
    print(a, b, c)

values_list = [1, 'None', True]
values_dict = {'a': 1, 'b': 'None', 'c': True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 15)
print_params(b = 25) 
print_params(c = [1,2,3]) 
