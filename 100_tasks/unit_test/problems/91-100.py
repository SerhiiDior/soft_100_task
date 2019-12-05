#91
def task_91():
    lst=[12,24,35,70,88,120,155]
    lst.remove(lst[0])
    lst.remove(lst[4])
    lst.remove(lst[5])
    return lst

#92
def task_92():
    lst=[12,24,35,70,88,120,155]
    lst.remove(24)
    return lst

#93
def task_93():
    lst1=[1,3,6,78,35,55]
    lst2=[12,24,35,24,88,120,155]
    res=[]
    for i in lst2:
        for j in lst1:
            if i==j:
                res.append(i)

#94
def task_94():
    lst=[12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    res=[]
    for x in lst:
        if x not in res:
            res.append(x)
    return res

#95
class Person:
    def getGender(self):
        print("Person")


class Male(Person):
    def getGender(self):
        print("Male")


class Female(Person):
    def getGender(self):
        print("Female")


male = Male()
female = Female()

#96
def task_96(string):
    st = set(string)
    dict = {i: string.count(i) for i in st}
    dict = {key: dict[key] for key in sorted(dict.keys())}
    for i in dict.keys():
        print(str(i) + "," + str(dict[i]))

#97
def task_97(x):
    return x[::-1]

#98
def task_98(x):
    return x[::2]

#99
def task_99():
        return list(itertools.permutations([1, 2, 3]))
#100
def task_100(head, leg):
    return("rabbits " + str(leg // 2 - head) + " chikens " + str(head - (leg // 2 - head)))
