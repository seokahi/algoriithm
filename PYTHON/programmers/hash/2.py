nums = [3,3,3,2,2,2]
N = round(len(nums)/2)
nums = set(nums)
print( N if N<len(nums) else len(nums))