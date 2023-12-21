n = int(input())
m=list(map(int,input().split()))
m.sort()
result = 0
cnt =0
for i in m:
    cnt += 1
    if(cnt>=i):
        cnt = 0
        result += 1

print(result)