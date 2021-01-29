'''739. 每日温度'''

# 请根据每日气温列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替

'''解法'''
# 1、索引进栈
# 2、当前元素和栈顶元素相比
# 遍历整个数组，如果栈不空，且当前数字大于栈顶元素，那么如果直接入栈的话就不是 递减栈 ，所以需要取出栈顶元素，由于当前数字大于栈顶元素的数字，而且一定是第一个大于栈顶元素的数，直接求出下标差就是二者的距离。
# 继续看新的栈顶元素，直到当前数字小于等于栈顶元素停止，然后将数字入栈，这样就可以一直保持递减栈，且每个数字和第一个大于它的数的距离也可以算出来。


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# nums = [2,1,2,4,3]
# nums = [4,2,4,0,0]
def dailyTemperatures(T):
    stack = []
    res = [0] * len(T)

    for i in range(len(T)):
        while stack and T[i] > T[stack[-1]]:
            index = stack.pop()
            res[index] = i - index
        stack.append(i)
    return res

print(dailyTemperatures(temperatures))