import sys

sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")
K, N = map(int, input().split(" "))
list=[]
for _ in range(K):
    list.append(input().split(" "))
fin=list[0]
list.pop(0)
ans=0
for i in range(N):
    pairs=[]
    for d in range(i+1, N):
        lis=[fin[i], fin[d]]
        pairs.append(lis)
    for bub in pairs:
        booles=True
        for fef in list:
            if fef.index(bub[0])>fef.index(bub[1]):
                booles=False
                break
        if booles:
            ans+=1
print(ans)