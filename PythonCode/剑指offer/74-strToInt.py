'''
分情况判断
1、空格
2、符号位
3、非数字字符
4、字符转数字拼接+超过最大的值进行判断
'''

def strToInt( str):
    res, i, sign, length = 0, 0, 1, len(str)
    int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
    if not str: return 0  # 空字符串，提前返回
    while str[i] == ' ':
        i += 1
        if i == length: return 0  # 字符串全为空格，提前返回
    if str[i] == '-': sign = -1
    if str[i] in '+-': i += 1
    for c in str[i:]:
        if not '0' <= c <= '9': break
        if res > bndry or res == bndry and c > '7': # 2 ** 31 - 1 最后一位是7
            return int_max if sign == 1 else int_min
        res = 10 * res + ord(c) - ord('0')
    return sign * res