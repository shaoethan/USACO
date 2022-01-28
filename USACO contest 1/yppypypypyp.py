import sys 
sys.stdin=open("square.in", "r")
sys.stdout=open("square.out", "w")
rect1=input().split()
rect2=input().split()
for i in range(len(rect1)):
    rect1[i]==int(rect1[i])
for p in range(len(rect2)):
    rect2[p]==int(rect2[p])
x1=int(rect1[0])
y1=int(rect1[1])
x2=int(rect1[2])
y2=int(rect1[3])
x3=int(rect2[0])
y3=int(rect2[1])   
x4=int(rect2[2])
y4=int(rect2[3])
leftpart=min(x1, x3)
bottompart=min(y1, y3) 
rightpart=max(x2, x4)      
toppart=max(y2, y4) 
sideleng= max(rightpart-leftpart, toppart-bottompart)
print(sideleng*sideleng)
    
    