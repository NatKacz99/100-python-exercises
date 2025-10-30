lst = [12, 24, 35, 70, 88, 120, 155]
li = list(filter(lambda number: number%35 != 0, lst))
print(li)