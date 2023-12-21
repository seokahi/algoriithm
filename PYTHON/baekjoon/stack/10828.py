import sys
n=int(input())
s=[]
for i in range(n):
    infrom=sys.stdin.readline().split()
    if(infrom[0] == "push"):
        s.append(int(infrom[1]))
    elif(infrom[0]=="pop"):
        if(len(s) ==0):
            print("-1")
        else:
            print(s[-1])
            s.pop()
    elif(infrom[0] == "top"):
        if(len(s) ==0):
            print("-1")
        else:
            print(s[-1])
    elif(infrom[0] =="size"):
        print(len(s))
    elif(infrom[0] == "empty"):
        if(len(s) ==0):
            print("1")
        else:
            print("0")
