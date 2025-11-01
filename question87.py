# solution 1
lst1 = [1,3,6,78,35,55]
lst2 = [12,24,35,24,88,120,155]

set1 = set(lst1)
set2 = set(lst2)

intersection = set1 & set2
print(intersection)

# solution 2
lst1 = [1,3,6,78,35,55]
lst2 = [12,24,35,24,88,120,155]

set1 = set(lst1)
set2 = set(lst2)

intersection = set.intersection(set1, set2)
print(intersection)