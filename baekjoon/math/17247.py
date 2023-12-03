
n,m=map(int,input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
current_x = -1
current_y = -1
flag = 0
for i in range(n):
    if flag == 1:break
    for j in range(m):
        if arr[i][j] == 1 and current_x == -1 and current_y ==-1:
            current_x = i
            current_y = j
        elif (arr[i][j] == 1):
            print(abs(current_x-i)+abs(current_y-j))
            flag = 1

            break


