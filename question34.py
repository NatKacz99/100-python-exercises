# python3
square_numbers = lambda: print([i**2 for i in range(1,21)][:5])

square_numbers()


# python2
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li[:5]

printList()
