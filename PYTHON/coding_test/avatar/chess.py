n=input()
steps=[(2,1),(2,-1),(-2,-1),(-2,-1),(1,-2),(-1,2),(1,2),(-1,-2)]
row = ord(n[0])-97+1

column = int(n[1])
cnt = 0
for x,y in steps:
    if(1<=row+x<=8 and 1<=column+y<=8):
        cnt += 1

print(cnt)                                                                                                                                                    