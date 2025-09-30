# Python3 solution

#using for loops
for i in range(2000, 3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')
        print("\b")

#Using generators and list comprehension
print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=", ")

# Python2
output = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        output.append(str(i))

print(', '.join(output))
