import math

x, y = 0, 0

while 1:
  user_input = input().split()
  if not user_input:
        break
  if user_input[0]=='UP':               
        x -= int(user_input[1])                
  if user_input[0]=='DOWN':
        x += int(user_input[1])
  if user_input[0]=='LEFT':
        y -= int(user_input[1])
  if user_input[0]=='RIGHT':
        y += int(user_input[1])
                                    
distance = round(math.sqrt(x**2 + y**2))  
print(distance)



