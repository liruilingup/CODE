import random

'''
解题思路：
https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/xiang-xi-si-lu-ji-you-hua-si-lu-fen-xi-zhu-xing-ji/
'''

'''
一、rand10生成rand7
    大于7的时候直接舍弃即可，等比数列可证明概率一样

二、rand7生成rand10
    rand7 = 1,2,3,4,5,6,7
    rand10 = 1,2,3,4,5,6,7,8,9,10
    如果：rand7+rand7 = [2~14] 但不是等概率
    等概率[0,1,2,3,4,6]*7 + [1,2,3,4,5,6,7] = [0~49] #如果不是7就会有重复的
    即：num = (random.randint(1,7) - 1) * 7 + random.randint(1,7) # 大于10的时候舍弃

'''
# 方法1、大于10的舍弃
def rand10():
    num = (random.randint(1,7) - 1) * 7 + random.randint(1,7)
    while num > 10:
        num = (random.randint(1,7) - 1) * 7 + random.randint(1,7)
    return num
print(rand10())


# 方法2、大于40的舍弃，1-40之间求余数
def rand10_2():
    num = (random.randint(1,7) - 1) * 7 + random.randint(1,7)
    while num > 40:
        num = (random.randint(1,7) - 1) * 7 + random.randint(1,7)
    # [1~10] % 10 是[1,2,3,4,5,6,7,8,9,0]， 所以加1
    return 1 + num % 10
print(rand10_2())


