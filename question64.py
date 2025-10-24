# solution 1
def generate(n):
  for i in range(n + 1):
    if i % 35 == 0:
      yield i

n = int(input())
response = [str(i) for i in generate(n)]
print(",".join(response))

# solution 2
def generate(n):
  for i in range(n + 1):
    if i%5 == 0 and i%7 == 0:
      yield i

n = int(input())
values = []
for i in generate(n):
  values.append(str(i))

print(",".join(values))