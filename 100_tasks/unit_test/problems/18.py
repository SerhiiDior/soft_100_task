def isUpper(x):
    for i in x:
        if 'A'<=i and i<='Z':
            return True
    return False
def isLower(x):
    for i in x:
        if 'a'<=i and i<='z':
            return True
    return False
def isNumber(x):
    for i in x:
        if '0'<=i and i<='9':
            return True
    return  False
def isSymbol(x):
    for i in x:
        if i=='$' or i=='#' or i=='@':
            return True
    return False
s=input("Passwords->").split(',')
lst=[]
for i in s:
    length=len(i)
    if 6<=length and length<=12 and isLower(i) and isUpper(i) and isNumber(i) and isSymbol(i):
        lst.append(i)
print(",".join(lst))
