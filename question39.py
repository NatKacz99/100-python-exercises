check_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_tuple = tuple(filter(lambda x: x % 2 == 0, check_tuple))
print(even_tuple)


