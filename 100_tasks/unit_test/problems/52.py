from math import pi
class Circle:
    def __init__(self,):
        pass
    def area(self):
        self.r = float( input( "Radius->" ) )
        return pi*(self.r**2)


circle=Circle()


if __name__ == '__main__':
    print( round( circle.area( ), 2 ) )

