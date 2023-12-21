d=[[0 for j in range(19)] for i in range(19)]

for i in range(19):
    a=list(map(int,input().split()))
    for j in range(19):
        d[i][j] = a[j]
        
n=int(input())
for i in range(n):
    x,y = map(int,input().split())
    for j in range(19):
        if(d[x-1][j] == 1):
            d[x-1][j] = 0
        else:
            d[x-1][j] =1
        if(d[j][y-1] == 1):
            d[j][y-1] = 0
        else:
            d[j][y-1]=1

for i in range(19):
    for j in range(19):
        print(d[i][j],end=" ")
    print() 