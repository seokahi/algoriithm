n=int(input())
result = [0]*24
a=list(map(int,input().split()))

for i in a:
    result[i-1] +=1
for i in range(23):
    print(result[i],end=" ")