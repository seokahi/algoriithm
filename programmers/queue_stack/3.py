stack = []


def solution(s):
    for i in s:
        if i =='(':
            stack.append('(')
        else:
            if(len(stack) ==0):
                return False
            if(stack[-1] == '('):
                stack.pop()
            else:
                stack.append(')')
    if len(stack) !=0 :
        return False
    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))