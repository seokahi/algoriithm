arr = [4,4,3,3,3]
def solution():
    # from collections import deque
    # stack = deque()
    # stack.append(arr[0])
    # for i in range(1,len(arr)):
    #     if stack[-1] != arr[i]:
    #         stack.append(arr[i])
    # return stack
    a=[]
    for i in arr:
        if a[-1:] != [i]:
            a.append(i)
    return a
print(solution())