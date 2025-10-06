# solution 1
lst = []
while True:
  x = input()
  if len(x) == 0:
    break
  lst.append(x)

balance = 0
for item in lst:
  if 'D' in item:
    balance += int(item.strip('D '))
  if 'W' in item:
    balance -= int(item.strip('W '))
print(balance)

# solution 2
lines = []
while True:
  loopInput = input()
  if loopInput == 'done':
    break
  else:
    lines.append(loopInput)

lst = list(int(i[2:]) if i[0] == 'D' else - int(i[2:]) for i in lines)
print(sum(lst))

# solution 3
money = 0
while 1:
  transaction = input().split(' ')
  if transaction[0] == 'D':
    money = money + int(transaction[1])
  elif transaction[0] == 'W':
    money = money - int(transaction[1])
  elif input() == '':
    break
print(f'Your current balnce is: {money}')