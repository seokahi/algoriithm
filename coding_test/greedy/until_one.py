n,k = map(int,input().split())
cnt = 0
# while 1:
#     while n%k ==0:
#         n = int(n/k)
#         cnt +=1
#         if(n==1):
#             break
#     if n ==1:
#         break
#     n -= 1
#     cnt +=1
# print(cnt)
while 1:
    target = int(n/k) *k
    cnt += (n-target)
    n = target
    if(n<k):
        break
    cnt +=1
    n//=k

cnt += n-1
print(cnt)