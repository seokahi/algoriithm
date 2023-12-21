list=[[0 for j in range(19)] for i in range(19)]
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    list[a-1][b-1] = 1

for i in range(19):
    for j in range(19):
        print(list[i][j],end=" ")
    print()
    # 줄바꿈은 print()로