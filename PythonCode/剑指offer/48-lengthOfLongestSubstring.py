# 方法一：动态规划 + 哈希表
def lengthOfLongestSubstring(s):
    dic = {}
    res = tmp = 0
    for j in range(len(s)):
        i = dic.get(s[j], -1)  # 获取索引 i
        dic[s[j]] = j  # 更新哈希表
        tmp = tmp + 1 if tmp < j - i else j - i  # dp[j - 1] -> dp[j]
        res = max(res, tmp)  # max(dp[j - 1], dp[j])
    return res
print('', lengthOfLongestSubstring('abcabcbb'))
# 方法二：使用双指针和哈希表
def lengthOfLongestSubstring2(s):
    dic, res, i = {}, 0, -1
    for j in range(len(s)):
        if s[j] in dic:
            i = max(dic[s[j]], i)  # 更新左指针 i
        dic[s[j]] = j  # 哈希表记录
        res = max(res, j - i)  # 更新结果
    return res
print('使用双指针和哈希表结果', lengthOfLongestSubstring2('abcabcbb'))

# 方法三：使用滑动窗口

def lengthOfLongestSubstring3(s):
    if len(s) == 1:return 1
    i=0
    j = 0
    res = 1
    while j < len(s)-1:
        j += 1
        if s[j] not in s[i: j]:
            res = max(j - i + 1, res)
        else:
            while s[j] in s[i: j]:
                i += 1
    return res

print('使用滑动窗口', lengthOfLongestSubstring3('abcabcbb'))
