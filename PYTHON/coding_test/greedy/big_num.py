n,m,k = map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
# sum = 0
# tmp = k
# for i in range(m):
#     if(tmp ==0):
#         sum += arr[len(arr)-2]
#         tmp = k
#     else:
#         sum += arr[len(arr)-1]
#         tmp -= 1
# print(sum)

# 2. 더 효율적인 코드
count = 0
count += int(m/(k+1))*k+m%(k+1)
result = 0
result += count*arr[len(arr)-1]
result += (m-count)*arr[len(arr)-2]
print(result)