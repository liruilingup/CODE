
def twoSum(nums, target):
    hashmap = {}
    for i, val in enumerate(nums):
        if hashmap.get(target-val) is not None:
            return [i, hashmap.get(target-val)]
        hashmap[val] = i

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))



