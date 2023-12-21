import math
W,H,X,Y,P = map(int,input().split())
cnt = 0
R = H/2
for i in range(P):
    x,y=map(int,input().split())
    if(X<=x<=X+W) and (Y<=y<=Y+H):
        cnt += 1
    else:
        d1 = math.sqrt((X-x)**2 + (Y+R-y)**2)
        d2 = math.sqrt(((X+W)-x)**2+((Y+R)-y)**2)
        if d1<=R or d2<=R:
            cnt += 1
print(cnt)