string=input("String-->").split(' ')
lst=[]
for i in string:
    for j in i:
        if "0"<=j and j<="9":
            lst.append(j)
print(lst)
