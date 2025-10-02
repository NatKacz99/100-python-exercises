#Solution1
user_input = input('Give two numbers separated by a comma: ')

if ',' not in user_input:
    print('Error: input must contain a comma')
else:
    x, y = map(int, user_input.split(',')) 
    output = []

    for i in range(x):
        tmp = []
        for j in range(y):
            tmp.append(i * j)
        output.append(tmp)

    print(output)

#Solution2:
user_input = input('Give two numbers separated by a comma: ')

if ',' not in user_input:
    print('Error: input must contain a comma')
else:
    x,y = map(int,input().split(','))
    output = [[i*j for j in range(y)] for i in range(x)]
    print(output)