from itertools import permutations
a=input().split(" ")
b = []
for i in a[0]:
    b.append(i)

i=list(permutations(b, int(a[1])))
for s in range(len(i)):
    temp=""
    curr=i[s]
    for er in range(int(a[1])):
        temp+=str(curr[er])
    i[s]=temp
i.sort()
for d in i: 
    string=""
    for e in range(int(a[1])):
        string+=d[e]
    print(string)