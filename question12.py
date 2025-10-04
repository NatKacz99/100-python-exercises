numbers_digit = []
for number in range(1000, 3001):  
    if all(int(digit) % 2 == 0 for digit in str(number)):
        numbers_digit.append(str(number))  

print(",".join(numbers_digit))
