'''121. 买卖股票的最佳时机'''
'''
1、记录最低点
2、利益是:当前值-最低值 和 最大利润比较
'''

def maxProfit(prices):
    profit = 0
    low = float('inf')
    for i in prices:
        low = min(i, low)
        profit = max(profit, i - low)
    return profit

