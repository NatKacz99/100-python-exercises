# solution 1
user_input = input('Enter your digit: ')
print(sum(int(i * user_input) for i in range(1, 5)))

# solution 2
user_input = input('Enter your digit: ')
total, tmp = 0, str()

for i in range(4):
  tmp += user_input
  total += int(tmp)

print(total)

# solution 3
user_input = input('Enter your digit: ')
total = int(user_input) + int(2 * user_input) + int(3 * user_input) + int(4 * user_input)
print(total)

# solution 4 
from functools import reduce
user_input = input('Enter your digit: ')
x = input('Please enter a digit: ')
reduce(lambda x, y: int(x) + int(y), [x * i for i in range(1, 5)])

# solution 5:
def calculate_sum(string_digit):
  return sum(int(string_digit * n) for n in range(1, 5))

user_input = input('Enter your digit: ')
print(calculate_sum(user_input))

# solution 6:
user_input = input('Enter your digit: ')
print(sum(int(i * user_input) for i in range(1,5)))