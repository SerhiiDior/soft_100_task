class Rectangle:
    def __init__(self):
        self.length=0
        self.width=0
    def area(self):
        return self.length*self.width

rectangle=Rectangle()
rectangle.length=int(input("Length="))
rectangle.width=int(input("Width="))
print(rectangle.area())
