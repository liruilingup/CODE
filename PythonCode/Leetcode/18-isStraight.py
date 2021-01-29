'''剑指 Offer 61. 扑克牌中的顺子'''
'''
1、判断0
2、判断重复的值
3、满足max()-min() < 5
'''

def isStraight(nums):
    mi = float('inf')
    ma = float('-inf')
    s = set()

    for i in nums:
        if i == 0:
            continue
        elif i in s:
            return False
        else:
            s.add(i)
            mi = min(i, mi)
            ma = max(ma, i)

    return ma - mi < 5

nums = [0,0,2,2,5]
print(isStraight(nums))


