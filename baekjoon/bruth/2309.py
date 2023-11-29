my_list = []
result = []
sum = 0
num_i =0
num_j=0

for i in range(9):
    n=int(input())
    my_list.append(n)
    sum += n


for i in range(0,9):
    for j in range(1,9):
        if(sum-(my_list[i]+my_list[j]) == 100):
            num_i = my_list[i]
            num_j = my_list[j]
            break


for i in my_list:
    if(num_i != i and num_j != i):
        result.append(i)

result.sort()

for i in result:
    print(i)
