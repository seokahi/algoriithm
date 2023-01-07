n,k=  map(int,input().split())
cnt = 0
# while n>=k:
#     while n%k !=0:
#         n-=1
#         cnt +=1
#     n//=k
#     cnt +=1
# while n!=1:
#     n-=1
#     cnt +=1

while 1:
    target = (n//k)*k
    cnt += (n-target)
    n=target
    if(n<k): break
    cnt += 1
    n //=k
cnt += (target-1)

print(cnt)
