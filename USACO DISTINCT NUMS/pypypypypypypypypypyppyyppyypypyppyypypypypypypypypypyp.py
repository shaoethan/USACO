num=1
gtyh=int(input())
numlist=input().split(" ")
for i in range(gtyh):
    numlist[i]=int(numlist[i])
numlist.sort()
beforenum=numlist[0]
for numindex in range(1, gtyh):
    if numlist[numindex] != beforenum:
        num+=1
        beforenum=numlist[numindex]
print(num)