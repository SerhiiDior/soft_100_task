class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length=0):
        Shape.__init__(self)
        self.length=length
    def area(self):
        return round((self.length*self.length),2)


length=float(input("Length->"))
square=Square(length)
print(square.area())
print(Square().area())
