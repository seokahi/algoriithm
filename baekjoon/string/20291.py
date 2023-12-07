n=int(input())
dic=dict()
for i in range(n):
    n=input().split(".")
    if(n[1] not in dic.keys()):
        dic[n[1]] = 1
    else : dic[n[1]]+=1
dic =dict(sorted(dic,key = lambda x:x[1]))
for k,v in dic.items():
    print(k,v)