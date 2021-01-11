'''
使用哈希
'''
def firstUniqChar(s):
    dic = {}
    for c in s:
        dic[c] = not c in dic
    for c in s:
        if dic[c]: return c
    return ' '