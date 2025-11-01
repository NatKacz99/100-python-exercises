lst = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

for i in lst:
    if lst.count(i) > 1:
        lst.remove(i)
print(lst)