words=input(":")
letters=0
digit=0
for i in words:
    if ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
        letters+=1
    if '0'<=i and i<='9':
        digit+=1
print("Letters-{}\nDigits-{}".format(letters,digit))
