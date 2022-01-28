leng=int(input())
dict={}
key=0
answerlist=[]
val=0
for i in range(leng):
    ing=input().split(" ")
    for i in range(len(ing)):
        ing[i] =int(ing[i])
    if ing[0] == 0:
        dict[ing[1]]=ing[2]
    elif ing[0]==1:
        if ing[1] in dict:
            answerlist.append(dict[ing[1]])
        else:
            print(0)
            
for p in answerlist:
    print(p)