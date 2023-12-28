from functools import reduce
from collections import Counter
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
def soultion():
    global clothes
    clothes = Counter(x[1] for x in clothes)
    return (reduce(lambda x,y:x*(1+y), clothes.values(),1)-1)
print(soultion())
