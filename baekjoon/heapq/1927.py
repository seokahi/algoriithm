import heapq
import sys
heap =[]
n=int(input())
for i in range(n):
    m=map=int(sys.stdin.readline().rstrip())
    if(m == 0 and len(heap) ==0):
        print("0")
    elif(m == 0):
        print((heapq.heappop(heap)))
    else:
        heapq.heappush(heap, m)