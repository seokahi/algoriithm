from collections import deque
import sys
queue = deque()
N=int(input())
for i in range(N):
    s = sys.stdin.readline().split()
    if(s[0] == "push"):
        queue.append(int(s[1]))
    elif(s[0]=="pop"):
        if(len(queue)==0):
            print("-1")
        else:
            print(queue[0])
            queue.popleft()
    elif(s[0] =="size"):
        print(len(queue))
    elif(s[0] =="empty"):
        if(len(queue)==0):
            print("1")
        else:
            print("0")
    elif(s[0]=="front"):
        if(len(queue)==0):
            print("-1")
        else:
            print(queue[0])
    else:
        if(len(queue) ==0):
            print("-1")
        else:
            print(queue[len(queue)-1])