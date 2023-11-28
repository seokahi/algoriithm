progresses =  [90,90]
speeds =  [10,9]
from collections import deque
import math
queue = []
result = []
a= []

cnt = 0
for i in range(len(progresses)):
    queue.append(math.ceil((100.0-progresses[i])/speeds[i]))
a.append(queue[0])
cnt += 1
for i in queue[1:]:
    if(max(a)<i):
        a.clear()
        a.append(i)
        result.append(cnt)
        cnt =1
    else:
        a.append(i)
        cnt += 1
result.append(cnt)
print(result)