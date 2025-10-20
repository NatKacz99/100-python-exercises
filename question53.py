entered_email = input("Enter email: ")

# solution 1
import re
pattern = r"(\w+)@\w+\.com"
match = re.search(pattern, entered_email)

if match:
    name = match.group(1)
    print(name)
else:
    print("Invalid email format")

# solution 2
email = entered_email.split('@')
print(email[0])
