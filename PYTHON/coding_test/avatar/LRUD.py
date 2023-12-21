dx=[0,0,-1,1]
dy=[-1,1,0,0]
x=1
y=1
n=int(input())

where = list(input().split())
for i in where:
    print(i)
    if i =="L":
        if(1<= y+dy[0]<=n):
            y= y+dy[0]
    elif i =="R":
        if(1<= y+dy[1]<=n):
            y= y+dy[1]
    elif i =="U":
        if(1<= x+dx[2]<=n):
            x= x+dx[2]
    else:
        if(1<= x+dx[3]<=n):
            x= x+dx[3]
print(x,y)