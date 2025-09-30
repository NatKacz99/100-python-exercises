try:
    number = int(input("Enter a number: "))
except ValueError as err:
    print(err)

#1
dictionary = {}
for i in range (1, number + 1):
    dictionary[i] = i * i
print(dictionary)

#2
dictionary = {i : i*i for i in range(1, number + 1)}
print(dictionary)

#3
print(dict(enumerate([i*i for i in range(1, number + 1)], 1)))