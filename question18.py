import re

user_input = input("Enter passwords: ").split(',')
pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$")

for single_password in user_input:
  if pattern.fullmatch(single_password):
    print(single_password)
