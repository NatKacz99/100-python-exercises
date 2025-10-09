lst = []

while True:
    user_input = input().split(',')
    if not user_input[0]:                          
        break
    lst.append(tuple(user_input))

lst.sort(key= lambda x:(x[0],int(x[1]),int(x[2]))) 
print(lst)



