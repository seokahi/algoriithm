hour = input()
min = "59"
sec = "59"
cnt = 0
for i in range(int(hour)+1):
    for j in range(int(min)+1):
        for k in range(int(sec)+1):
            time = ''.join(str(i)+str(j)+str(k))
            if '3' in time:
                cnt +=1
print(cnt)