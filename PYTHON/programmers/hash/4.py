from collections import defaultdict
from collections import Counter

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
cloth = defaultdict(int)
def solution(clothes):
    result = 1
    cloth = Counter(ctype for _,ctype in clothes)
    print(cloth)
    # for i in clothes:
    #     cloth[i[1]]+=1
    # for i in cloth.values():
    #     result *= (i+1)
    # return result -1
solution(clothes)