h,w = map(int,input().split())
list = [[0 for j in range(w)] for i in range(h)]
n = int(input())
for i in range(n):
    l,d,x,y= map(int,input().split())
    for i in range(l):
        if(d==0):
            list[x-1][y-1] = 1
            y+=1
        else:
            list[x-1][y-1] = 1
            x+=1
    
for i in range(h):
    for j in range(w):
        print(list[i][j],end= " ")
    print()