'''331. 验证二叉树的前序序列化'''

# 通过判断剪枝是否成功来判断是否是序列化的二叉树
def IsValidSerialization(preorder):
    res = preorder.split(',')
    stack = []
    for i in res:
        stack.append(i)
        while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append('#')
    return stack == ['#']
print('判断是否是序列化的二叉树:', IsValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
