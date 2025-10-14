# python3
def square_numbers():
    lst = [i ** 2 for i in range(1, 21)]
    print(tuple(lst))

square_numbers()

# python2
def square_numbers():
  lst = list()
  for i in range(1, 21):
		  lst.append(i**2)
	print tuple(lst)

square_numbers()