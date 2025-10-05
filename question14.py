input_user = input('Enter input: ')
upper, lower = 0, 0

for i in input_user:
    if 'a' <= i and i <= 'z' :
        lower += 1
    if 'A' <= i and i <= 'Z':
        upper += 1

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))