from collections import deque
import sys
queue = deque()
N=int(input())
for i in range(N):
    a=sys.stdin.readline().rstrip().split()
    if(a[0]=="1"):
        queue.appendleft(a[1])
    elif(a[0] =="2"):
        queue.append(a[1])
    elif(a[0]=="3"):
        if(len(queue) ==0):
            print("-1")
        else:
            print(queue.popleft())
    elif(a[0]=="4"):
        if(len(queue)==0):
            print("-1")
        else:
            print(queue.pop())
    elif(a[0]=="5"):
        print(len(queue))
    elif(a[0] =="6"):
        if(len(queue) ==0):
            print("1")
        else:
            print("0")
    elif(a[0]=="7"):
        if(len(queue) ==0):
            print("-1")
        else:
            print(queue[0])
    else:
        if(len(queue)==0):
            print("-1")
        else:
            print(queue[len(queue)-1])