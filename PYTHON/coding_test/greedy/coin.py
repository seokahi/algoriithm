n=1260
coins = [500,100,50,10]
cnt = 0
for i in coins:
    cnt += n // i
    n %= i
print(cnt)