class Test:
    def generator(self,n):
        return [i for i in range(n) if i%7==0] 
n = int(input())
num = Test()
lst = num.generator(n)
print(lst)
