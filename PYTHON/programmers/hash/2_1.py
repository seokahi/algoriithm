nums = [3,3,3,2,2,2]

def soultion():
    nums_set = set(nums)
    return round(len(nums)/2) if round(len(nums)/2)<len(nums_set) else len(nums_set)

print(soultion())