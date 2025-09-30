# solution 1
number = int(input())

factorial = 1 
i = 1
while i <= number:
    factorial = factorial * i;
    i = i + 1
print(factorial)

# solution 2
from functools import reduce

def fun(acc, item):
	return acc*item

num = int(input())
print(reduce(fun, range(1, num+1)))

# solution 3
number = int(input())
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i
print(factorial)

# solution 4
number = int(input())
def calculateFactorial(x): return 1 if x <= 1 else x * calculateFactorial(x - 1)
print(calculateFactorial(number))




