# solution 1
lst = [12, 24, 35, 70, 88, 120, 155]
new_list = [lst[i] for i in range(len(lst)) if i not in (0, 4, 5)]
print(new_list)

# solution 2
lst = [12, 24, 35, 70, 88, 120, 155]
print(lst(j for i, j in enumerate(lst) if i != 0 and i != 4 and i != 5))