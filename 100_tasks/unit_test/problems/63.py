while True:
    n=int(input("n="))
    if n>0:
        break
    else:
        n=int(input("n="))
sum=0
for i in range(1,n+1):
    sum+=(i/(i+1))
print("Sum=",round(sum,2))
