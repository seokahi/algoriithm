import sys
k=int(input())
stack = []
sum =0
for i in range(k):
    n=sys.stdin.readline().rstrip()

    if(n== "0"):
        stack.pop()
    else:
        stack.append(n)

if(len(stack) ==0):
    print("0")
else:
    for i in stack:
        sum +=int(i)
    print(sum)