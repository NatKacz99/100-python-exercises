# python3
def even(x):
   return x % 2 == 0


even_numbers = filter(even, range(1, 21))
print(list(even_numbers))

# python2
evenNumbers = filter(lambda x: x % 2==0, range(1, 21))
print evenNumbers
