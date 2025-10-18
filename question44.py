# python3
def calculate(x):
    return x * x

squared_numbers = list(map(calculate, range(1,21)))
print(squared_numbers)

# python2
squared_numbers  = map(lambda x: x**2, range(1,21))
print squared_numbers