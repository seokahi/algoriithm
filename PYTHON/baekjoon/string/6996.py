n=int(input())
for i in range(n):
    n,m=input().split()
    nn=sorted(n)
    print(nn)
    mm=sorted(m)
    print(mm)
    if(nn==mm):
        print(n,"&",m,"are anagrams.")
    else:
        print(n,"&",m,"are NOT anagrams.")