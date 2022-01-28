import sys
sys.stdin = open("blocks.in", "r")
sys.stdout=open("blocks.out","w")
N=int(input())
string=[]
for _ in range(N):
    shsh=input().split(" ")
    string.append(shsh)
ans={"a":0,
"b":0,
"c":0,
"d":0,
"e":0,
"f":0,
"g":0,
"h":0,
"i":0,
"j":0,
"k":0,
"l":0,
"m":0,
"n":0,
"o":0,
"p":0,
"q":0,
"r":0,
"s":0,
"t":0,
"u":0,
"v":0,
"w":0,
"x":0,
"y":0,
"z":0}

for i in ans:
    temp=0
    for d in string:
        temp+=max(d[0].count(i), d[1].count(i))
    ans[i]=temp
for i in ans:
    print(ans[i])

