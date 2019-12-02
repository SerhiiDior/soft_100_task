def compare(a,b):
    if len(a)>len(b):
        return a
    elif len(a)<len(b):
        return b
    elif len(a)==len(b):
        return a+' '+b

a=str(input("A->"))
b=str(input("B->"))

print(compare(a,b))
