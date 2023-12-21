graph = [[0 for j in range(10)] for i in range(10)]
for i in range(10):
    a= list(map(int,input().split()))
    for j in range(10):
        graph[i][j]= a[j]
x=1
y=1
graph[x][y] = 9
flag = 0
for i in range(1,10):
    if flag==1 :
        break
    for j in range(1,10):
        if(x+1>=10 or y+1>=10):
            flag = 1
            break
        if(graph[x][y+1] !=1):
            if(graph[x][y+1] ==2):
                graph[x][y+1] = 9
                flag = 1
                break
            y+=1
            graph[x][y] =9

        elif(graph[x+1][y]!=1):
             if(graph[x+1][y] ==2):
                graph[x+1][y] = 9
                flag = 1
                break
             x+=1
             graph[x][y] =9
        
for i in range(10):
    for j in range(10):
        print(graph[i][j],end=" ")
    
    print()
