import sys
n=int(input())
number = 1
stack = []
flag = 0
s= map(int,sys.stdin.readline().split())
for i in s:
    stack.append(i)
    while len(stack)!=0 and stack[-1] == number: 
        stack.pop()
        number +=1
print("Nice" if len(stack) ==0 else "Sad")