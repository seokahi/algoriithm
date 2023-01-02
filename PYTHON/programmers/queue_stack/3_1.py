def solution():
    s=")()("
    from collections import deque
    stack = deque()
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
    if len(stack) == 0:
        return True
    else: 
        return False

print(solution())