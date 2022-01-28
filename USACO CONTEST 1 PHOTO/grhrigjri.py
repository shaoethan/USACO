N=int(input())
string=input()
ans=0


for i in range(N-2):#n=3
    Hcount=0
    Gcount=0
    count = 0
    for p in string[i:N]:
        if p=='H':
            Hcount=Hcount + 1
        else:
            Gcount=Gcount + 1
        if count >=2:
            if Hcount==1 or Gcount==1:
                ans+=1
            elif Hcount>1 and Gcount>1:
                break
        count+=1
                 
print(ans)
