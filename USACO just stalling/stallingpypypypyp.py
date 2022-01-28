def check(a, b):
    N=len(a)
    for i in range(N):
        currenthorse=a[i]
        currentstall=b[i]
        


N=int(input())
a= input().split(" ")
b=input().split(" ")
for i in range(N):
    a[i]=int(a[i])
    b[i]=int(b[i])

total=0
#for i in range(N):
#    current=a[i]
#    for d in range(N):
#        second=b[d]
#        if current>=second:
#                total+=1
#print(total)
for i in range(N):
    currenthorse=a[i]
    currentstall=b[i]
    if currenthorse<=currentstall:
        