import re

email=input("Email->")
pattern = "\w+@(\w+).com"
ans = re.findall(pattern,email)
print(ans)
