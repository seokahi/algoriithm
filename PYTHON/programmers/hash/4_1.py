from collections import Counter
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]


def soultion():
    global clothes
    clothes = Counter(dict(clothes).values())
    cnt = 1
    for value in clothes.values():
        cnt *=1+value
    return cnt-1
print(soultion())
