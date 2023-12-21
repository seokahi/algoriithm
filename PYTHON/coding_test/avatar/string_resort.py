s=input()
sum = 0
new = ""
for i in s:
    if '0'<=i<='9':
        sum += int(i)
    else:
        new += i
if(sum !=0): result = ''.join(sorted(new))+str(sum)
else : result =''.join(sorted(new))

print(result)