# import sys
# while(1):
#     stack = []
#     flag = 0
#     ins = sys.stdin.readline().rstrip()
#     if(len(ins) ==1 and ins[0] =="."):
#         break
#     for s in ins:
#         if flag == 1:
#             break
#         if(s=='.' and len(stack) == 0):
#             print("yes")
#             break
#         elif(s=='.' and len(stack) != 0):
#             print("no")
#             break
#         if(len(stack) ==0 and s=="]" or len(stack) ==0 and s==')'):
#             print("no")
#             flag = 1
#             continue
#         if(s =='['):
#             stack.append('[')
#         elif(s =='('):
#             stack.append('(')
#         elif(s ==']'):
#             if(stack[-1] == '['):
#                 stack.pop()
#             else:
#                 print("no")
#                 flag = 1
#                 continue
#         # 문자가 오니까 무조건 else로 올것임. -> elli
#         elif(s==')'):
#             if(stack[-1] == '('):
#                 stack.pop()
#             else:
#                 print("no")
#                 flag = 1
#                 continue
import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s[0]=='.': break
    s = ''.join([i for i in s if i in ['(',')','[',']']])
    while '()'in s or '[]' in s:
        s=s.replace('()','')
        s=s.replace('[]','')
    print('no' if len(s) else 'yes')