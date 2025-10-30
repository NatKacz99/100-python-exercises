# solution 1
lst = [12, 24, 35, 70, 88, 120, 155]
indices = [0, 2, 4, 6]

new_list = [i for (j, i) in enumerate(lst) if j not in indices]
print(new_list)

# solution 2
lst = [12, 24, 35, 70, 88, 120, 155]
lst = [lst[i] for i in range(len(lst)) if i%2 != 0 and i <= 6]
print(lst)