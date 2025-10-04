# Solution 1
user_input = input().split()

for i in user_input:
    if user_input.count(i) > 1:
        user_input.remove(i)

user_input.sort()
print(" ".join(user_input))

# Solution 2
user_input = input().split()
output = []

for words in user_input:
  if words not in output:
    output.append(words)
print(" ".join(sorted(output)))
