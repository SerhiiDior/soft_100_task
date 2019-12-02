def EvenGenerator(n):
    i=0
    while i<=n:
        if i%5==0 and i%7==0:
            yield i
        i+=1


n=int(input("n="))
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print (",".join(values))
