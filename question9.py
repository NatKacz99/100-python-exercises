user_input_capitalized = []

print("Give sequence of lines:")
while True:
  user_input = input()
  if len(user_input) == 0:
    break
  else:
    user_input_capitalized.append(user_input.upper())

for line in user_input_capitalized:
  print(line)

