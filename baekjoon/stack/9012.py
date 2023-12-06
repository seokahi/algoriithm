import sys
T = int(input())
for i in range(T):
    stack = []
    s=sys.stdin.readline().strip()
    for i in s:
        if(i=="("):
            stack.append("(")
        else:
            if(len(stack)==0):
                stack.append(")")
                break
            else:
                stack.pop()
    if(len(stack) ==0):
        print("YES")
    else:
        print("NO")