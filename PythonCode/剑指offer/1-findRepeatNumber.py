# 方法一、哈希表
# 方法二、原地交换(跟索引有关系)

'''使用方法2'''
def findRepeatNumber(nums):
    i = 0
    while i < len(nums):
        if nums[i] == i:
            i += 1
            continue
        if nums[nums[i]] == nums[i]:return nums[i] # 说明重复了
        nums[nums[i]], nums[i] = nums[i], nums[nums[i]] # 第一次遇到x时，交换到x处，第二次遇到时候，就重复了。
    return -1

nums = [0,2,1,4,4,1,1,1]
print('结果：', findRepeatNumber(nums))