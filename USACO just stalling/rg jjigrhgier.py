N=int(input())
for i in range(N):
    current=input().split(" ")
    if current[1].isnumeric():
        if int(current[1])!=0:
            print(int(current[0])/int(current[1]))
        else:
            print("Error Code: integer division or modulo by zero")
    else:
        if current[0].isnumeric:
            print("Error Code: invalid literal for int() with base 10: "+"'"+current[1]+"'")
        else:
            print("Error Code: invalid literal for int() with base 10: "+"'"+current[0]+"'")