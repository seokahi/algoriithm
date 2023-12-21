# from collections import deque
# n=int(input())
# queue = deque([i for i in range(1,n+1)])
# queue_1=deque(list(map(int,input().split())))
# result =[]
# current_num = 1
# while(len(queue)!=0):
#     result.append(current_num)
#     move= queue_1[current_num-1]
#     queue.rotate(-move)
#     if(queue[0] == current_num):
#         if move <0:
#             queue.rotate(1)
#         else: 
#             queue.rotate(-1)
#     queue.remove(current_num)
#     if(len(queue) ==0) :break
#     current_num = queue[0]

# for i in result:
#     print(i,end=" ")
from collections import deque
qeue = deque([1,2,3,4,5])
qeue.rotate(1)
print(qeue)