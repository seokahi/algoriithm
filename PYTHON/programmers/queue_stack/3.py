priorities = [1, 1, 9, 1, 1, 1]
location = 0
def solution(priorities, location):
    from collections import deque
    priorities = deque(priorities)
    process = deque()
    result = deque()
    for i in range(0,len(priorities)):
        process.append(chr(65+i))
    while len(process)!=0:
        if len(process) == 1:
            result.append(process[0])
            priorities.popleft()
            process.popleft()
            break
        if priorities[0] >= max(list(priorities)[1:]):
            result.append(process[0])
            priorities.popleft()
            process.popleft()
            
        else:
            priorities.append(priorities.popleft())
            process.append(process.popleft())     
    return result.index(chr(65+location))+1

print(solution(priorities,location))
