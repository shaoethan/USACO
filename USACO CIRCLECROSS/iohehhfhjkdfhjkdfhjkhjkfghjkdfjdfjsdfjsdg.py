import sys
sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")
hef=input()
letters=hef
ans=0   
for i in range(len(letters)-1):
    for p in range(i+1, len(letters)):
        if not letters[p]==letters[i] and p!=len(letters)-1:
            sub=letters[p+1:]
            cheese1=sub.find(letters[p])
            cheese2=sub.find(letters[i])
            if cheese1!= -1 and cheese2!=-1 and cheese1>cheese2:
                    ans+=1
print(ans)