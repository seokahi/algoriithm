import heapq
import sys
minus_heap = []
plus_heap= []
n=int(input())
for i in range(n):
    num=int(sys.stdin.readline().rstrip())
    if(num<0): heapq.heappush(minus_heap,-num)
    elif(num>0): heapq.heappush(plus_heap,num)
    else:
        if(len(minus_heap) ==0 and len(plus_heap)==0):
            print("0")
        
        elif(len(minus_heap) !=0 and len(plus_heap)!=0):
            if (minus_heap[0]==plus_heap[0]):
                print(-heapq.heappop(minus_heap))
            elif(minus_heap[0] <plus_heap[0]):
                print(-heapq.heappop(minus_heap))
            else:
                print(heapq.heappop(plus_heap))
        elif(len(minus_heap)==0 and len(plus_heap)!=0):
            print(heapq.heappop(plus_heap))
        elif(len(plus_heap)==0 and len(minus_heap)!=0):
            print(-heapq.heappop(minus_heap))