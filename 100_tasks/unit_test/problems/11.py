numbers=input("Numbers->").split(',')
numbers=[int(i) for i in numbers]
for i in numbers:
    if i%5==0:
        print(i,end='\n')
