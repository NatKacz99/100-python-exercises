# solution 1
square_numbers = lambda: print([i**2 for i in range(1, 21)][-5:])

square_numbers()

# solution 2
def square_numbers():
    lst = [i ** 2 for i in range(1, 21)]
    for i in range(19,14,-1):
        print(lst[i])

square_numbers()

