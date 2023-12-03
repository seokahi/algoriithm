n=int(input())
arr= [list(map(int,input().split())) for _ in range(n)]
arr.append(arr[0])
sum =0
for i in range(n):
    x=abs(arr[i+1][0]-arr[i][0])
    y=abs(arr[i+1][1]-arr[i][1])
    sum += x+y

print(sum)