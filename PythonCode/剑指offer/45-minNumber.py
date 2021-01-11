# 本质是排序问题
# 字符串排序： x + y < y + x 才可以得出 x <y ， 在快排的条件下改下

def minNumber(nums):
    def fast_sort(l, r):
        if l >= r: return
        i, j = l, r
        while i < j:
            while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
            while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
            strs[i], strs[j] = strs[j], strs[i]
        strs[i], strs[l] = strs[l], strs[i]
        fast_sort(l, i - 1)
        fast_sort(i + 1, r)

    strs = [str(num) for num in nums]
    fast_sort(0, len(strs) - 1)
    return ''.join(strs)