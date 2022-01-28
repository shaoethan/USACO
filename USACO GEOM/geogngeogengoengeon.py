import sys
sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out","w")
N, M=map(int,input().split(" "))
spotted=[]
plain=[]
for _ in range(N):
    spotted.append(input())
for _ in range(N):
    plain.append(input())
ans=0

for i in range(M):
    currents=[]
    currentp=[]
    for d in spotted:
        currents.append(d[i])
    for e in plain:
        currentp.append(e[i])
    breakbool=False
    for fe in currents:
        if fe in currentp:
            breakbool=True
            break
    if not breakbool:
        ans+=1
print(ans)














'''
for i in range(M):
    current=[]
    for geonome in plain:
        current.append(geonome[i])
    if current.count(current[0])==len(current):
        yess=current[0]
        counter=0
        current=[]
        for curr in spotted:
            current.append(curr[i])
        for p in current:
            if not p==yess:
                counter+=1
        if counter==len(current):
            ans+=1
'''