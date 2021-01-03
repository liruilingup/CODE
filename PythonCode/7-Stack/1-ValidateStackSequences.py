'''验证栈的序列'''
def ValidateStackSequences(pushed, popped):
    stack = []
    for i in pushed:
        stack.append(i)
        while stack and stack[-1] == popped[0]:
            popped.pop(0)
            stack.pop()
    return not stack

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print('栈的序列', ValidateStackSequences(pushed, popped))



