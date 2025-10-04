user_numbers = input("Input 4 digit binary numbers separated a comma: ").split(',')

# solution 1
def check_if_divided(x):
    return int(x, 2) % 5 == 0                                

data = list(filter(check_if_divided, user_numbers))
print(",".join(data))

# solution 2
user_numbers = list(filter(lambda i:int(i,2)%5==0, user_numbers))
print(user_numbers)
