import re
entered_email = input("Enter email: ")

pattern = r"\w+@(\w+)\.com"
company_name = re.findall(pattern, entered_email)
print(company_name)