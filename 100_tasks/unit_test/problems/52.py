from math import pi
class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return pi*(self.radius**2)

r=float(input("Radius->"))
circle=Circle(r)
print(round(circle.area(),2))
