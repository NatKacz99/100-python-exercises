# solution 1
import re
entered_sentence = input()
pattern = r"\d+"
digits = re.findall(pattern, entered_sentence)
print(digits)

# solution 2
email = input().split()
ans = [word for word in email if word.isdigit()]  
print(ans)