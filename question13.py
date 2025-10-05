user_input = input('Enter your sentece: ')

letter, digit = 0, 0

for i in user_input:
    if ('a' <= i and i <= 'z') or ('A' <=i and i <=' Z'):
        letter += 1
    if '0' <= i and i <= '9':
        digit += 1

print("LETTERS {0}\nDIGITS {1}".format(letter, digit))
