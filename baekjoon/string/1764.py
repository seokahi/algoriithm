import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
L=set()
S=set()
result = []
for i in range(n):
    s=sys.stdin.readline().rstrip()
    L.add(s)
for j in range(m):
    s=input()
    S.add(s)
for i in L:
    if i in S:
        result.append(i)

result.sort()
print(len(result))
for i in result:
    print(i)