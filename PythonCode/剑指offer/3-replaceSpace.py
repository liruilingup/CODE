
'''剑指 Offer 05. 替换空格'''
# 方法一：使用新的数组长度是s的三倍，重新构建
# 方法二：优化，c++中字符串可以变化长度，可以使用
def replaceSpace(s):
    res = []
    for c in s:
        if c == ' ':
            res.append("%20")
        else:
            res.append(c)
    return "".join(res)

s = '"We are happy."'
print('遍历方法的结果', replaceSpace(s))

# 方法2,如果字符串可以被修改
# 1、先统计空格的个数
# 2、修改s的长度
# 3、倒着移动
