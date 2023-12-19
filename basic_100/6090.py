a,m,d,n=map(int,input().split())
sum = a
for i in range(n-1):
    sum *= m
    sum += d
print(sum)