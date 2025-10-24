# solution 1
def even_numbers(n):
  i = 0
  while i <= n:
    if i % 2 == 0:
      yield i
    i += 1

n = int(input())
values = []
for i in even_numbers(n):
  values.append(str(i))

print(",".join(values))

# solution 2
n = int(input())

for i in range(0, n + 1, 2):
  if i < n - 1:
    print(i, end = ',' )
  else:
    print(i)