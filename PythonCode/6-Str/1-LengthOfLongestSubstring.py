'''3. 无重复字符的最长子串'''

# 采用滑动窗口的方法来解决
# 输入: s = "abcabcbb"
# 输出: 3


def lengthOfLongestSubstring(s):
    # 哈希集合，记录每个字符是否出现过
    occ = set()
    n = len(s)
    # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
    ans = 0
    right = 0
    for left in range(n):
        if left != 0:
            # 说明重复了，左指针向右移动一格，移除一个字符
            occ.remove(s[left - 1])
        while right < n and s[right] not in occ: # 不断地移动右指针
            occ.add(s[right])
            right += 1
        # 第 i 到 rk 个字符是一个极长的无重复字符子串
        ans = max(ans, right - left)
    return ans
s = "abcabcbb"
print(lengthOfLongestSubstring(s))
