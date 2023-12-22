from collections import deque

priorites = [2,1,3,2]
location = 2

number = deque()
result = deque()
alpha = 65

for i in range(len(priorites)):
    number.append(chr(alpha))
    alpha += 1

priority = deque(priorites)

compare = 0
for i in priority:
    if(compare+1 <len(priority)-1):
        compare +=1
    list = deque(list(priority)[compare:])
    compare_num = max(list)
    print(compare_num)
    if(compare>i):
        num1 = number.popleft()
        number.append(num1)
        num2 = priority.popleft()
        priority.append(num2)
    else:
        result.append(number.popleft())
        priority.popleft()
    

# print(result)

