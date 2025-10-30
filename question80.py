# solution 1
# def isEven(number):
#     return number%2 != 0

# li = [5, 6, 77, 45, 22, 12, 24]
# lst = list(filter(isEven, li))
# print(lst)

# solution 2
li = [5, 6, 77, 45, 22, 12, 24]
lst = list(filter(lambda number: number%2 != 0, li))
print(lst)