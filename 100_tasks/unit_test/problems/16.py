numbers=map(int,input("Numbers->").split(','))
for i in numbers:
    if i%2!=0:
        print(i,end=',')
