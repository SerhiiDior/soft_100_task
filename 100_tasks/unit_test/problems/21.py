import math
class Robot():
    x=0
    y=0
    def __init__(self):
        x=0
        y=0
    def distance(self):
        dist=math.sqrt(((self.x-0)**2)+((self.y-0)**2))
        return dist

total = Robot()
while True:
    s = input().split()
    if not s:
        break
    cm,num = map(str,s)

    if cm=='UP':
        total.y+=int(num)
    if cm=='DOWN':
        total.y-=int(num)
    if cm=='LEFT':
        total.x-=int(num)
    if cm=='RIGHT':
        total.x+=int(num)
        
print("Res=",round(total.distance()))
