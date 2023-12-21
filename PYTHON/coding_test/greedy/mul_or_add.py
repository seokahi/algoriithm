s=input()
first = int(s[0])
n = first
for i in range(1,len(s)):
    if(n!=0 and int(s[i])!=0):
        n = int(n)*int(s[i])
    else:
        n = int(n)+int(s[i])
print(n)
