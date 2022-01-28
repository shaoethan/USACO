x,k=map(int, input().split(" "))
poly=input().split(" ")
ans=0
for i in range(len(poly)):
    current=poly[i]
    if "**" in current and "*x**" not in current:
        if not poly[i-1]=="-":
            ans+=(x**int(current[3]))
        elif poly[i-1]=="-":
            ans-=(x**int(current[3]))
    elif current=="+":
        if not "**" in poly[i+1]:
            if not poly[i+1]=="x":
                ans+=int(poly[i+1])
            else: 
                ans+=x
    elif current=="-":
        if not "**" in poly[i+1]:
            if not poly[i+1]=="x":
                ans-=int(poly[i+1])
            else:
                ans-=x
    elif "*x**"in current:
        if poly[i-1]=="+":
            ans+=int(current[0])*(x**int(current[5]))
        elif poly[i-1]=="-":
            ans-=int(current[0])*(x**int(current[5]))
                
if ans==k:
    print("True")
else:
    print("False")
