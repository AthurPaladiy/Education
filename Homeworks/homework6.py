my_dict = {'Vasya': 1984, 'Petya': 1990, 'Edgar': 1999}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Petya'))
print('Not existing value:', my_dict.get('Egor'))
print('Deleted value:', my_dict.pop('Edgar'))
print('Modified dictionary:', my_dict)
print('\n')
my_set = {1, 1, 0.5, 0.5, 'Тыблоко', 'Тыблоко'}
print('Set:', my_set)
my_set.update([4, 'Червь'])
my_set.remove(0.5)
print('Modified set:', my_set)
