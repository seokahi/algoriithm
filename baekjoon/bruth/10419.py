T=int(input())
for i in range(T):
    d=int(input())
    t=1
    while 1:
        s=t*t
        if(s+t>d):
            break
        t+=1

    print(t-1)