user_input = input().split(',')

output = []
user_input = [int(i) for i in user_input]
for i in user_input:
    if i % 2 != 0:
        output.append(i ** 2)

print(output)
