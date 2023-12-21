import sys
n=int(input())
for i in range(n):
    num=sys.stdin.readline().rstrip()
    cnt = 0
    while num!="6174":
        max=''.join(sorted(num,reverse=True))
        min=''.join(sorted(num))
        num= int(max) - int(min)
        num=str(num)
        cnt +=1
        if(len(num)<4):
            num +="0"*(4-len(num))
    print(cnt)

    