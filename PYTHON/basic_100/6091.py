a,b,c= map(int,input().split())
n=1
while 1:
    if(n%a == 0 and n%b==0 and n%c==0):
        print(n)
        break
    n+=1