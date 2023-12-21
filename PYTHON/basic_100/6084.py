h,b,c,s=map(int,input().split())
result =(h*b*c/8/1024/1024)*s
print(round(result,1),"MB")