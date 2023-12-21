import math
n=int(input())
arr=[list(input().split()) for _ in range(n)]

cnt  = 0
for i in range(n):
    for j in range(n):
        if(arr[i][j]=='5'):
            t_x = i
            t_y = j
        elif(arr[i][j] == '2'):
            s_x = i
            s_y = j
min_x = min(t_x,s_x)
max_x = max(t_x,s_x)
min_y = min(t_y,s_y)
max_y = max(t_y,s_y)
if(math.sqrt((max_x-min_x)*(max_x-min_x)+(max_y-min_y)*(max_y-min_y))>=5):
    for i in range(min_x,max_x+1):
        for j in range(min_y,max_y+1):
            if(arr[i][j] == '1'):
                cnt += 1
    if(cnt>=3):
        print("1")
    else:
        print("0")
else:
    print("0")