dic = {"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
dic_rev = {v:k for k,v in dic.items()}
n,m=input().split()
arr=[str(i) for i in range(int(n),int(m)+1)]
eng_arr=[]
kor_arr=[]
for i in arr:
    eng_num =""
    for j in i:
        eng_num += dic[j]
        eng_num += " "
    eng_arr.append(eng_num)

eng_arr =sorted(eng_arr)
for i in eng_arr:
    kor_num=""
    for j in i.split():
        kor_num+=dic_rev[j] 

    kor_arr.append(int(kor_num)) 
for i in range(0, len(kor_arr), 10):
	print(*kor_arr[i:i+10])

# 다른 풀이
dic = {"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
n,m=map(int,input().split())
arr=[str(i) for i in range(n,m+1)]
eng_arr=[]
for i in arr:
    eng_num =""
    s=list(i)
    for j in s:
         eng_num +=dic[j]
    eng_arr.append((eng_num,i))
eng_arr.sort(key=lambda x:x[0])
kor_arr=[i[1] for i in eng_arr]
for i in range(0, len(kor_arr), 10):
	print(*kor_arr[i:i+10])