words=input(":")
upper=0
lower=0
for i in words:
    if ('a'<=i and i<='z'):
        lower+=1
    if ('A'<=i and i<='Z'):
        upper+=1
print("Upper-{}\nLower-{}".format(upper,lower))
