from collections import deque
n,k=map(int,input().split())
arr = deque([ i for i in range(1,n+1)])
queue=deque()
while(len(arr)!=0):
    arr.rotate(-(k-1))
    queue.append(str(arr.popleft()))

print("<",", ".join(queue),">",sep="")
