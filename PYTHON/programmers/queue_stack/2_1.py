progresses = [90, 90, 90, 90]
speeds = 	[30, 1, 1, 1]

def solution():
    from math import ceil
    develop = []
    result = []
    stack = []
    for i in range(len(progresses)):
        develop.append(ceil((100 - progresses[i])/speeds[i]))
    stack.append(develop[0])
    cnt = 1
    for i in develop[1:]:
        if(max(stack)>=i):
            stack.append(i)
            cnt += 1
        else:
            result.append(cnt)
            stack.clear()
            stack.append(i)
            cnt = 1
    result.append(cnt)
    return result

print(solution())
