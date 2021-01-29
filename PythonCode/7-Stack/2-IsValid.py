
'''给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。'''
# 1、左括号进栈
# 2、栈顶元素跟右括号匹配时出栈



def IsValid(s):
    dict1 = {')':'(', ']':'[', '}':'{'}
    stack = []

    for string in s:
        if stack and string in dict1:
            if stack[-1] == dict1[string]:
                stack.pop()
            else:
                return False
        else:
            stack.append(string)
    return not stack

s = "()[]{}"

print(IsValid(s))