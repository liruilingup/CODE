def validateStackSequences(pushed, popped):
    stack = []
    for i in pushed:
        stack.append(i)
        while stack and stack[-1] == popped[0]:
            stack.pop()
            popped.pop(0)
    return not popped

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(validateStackSequences(pushed, popped))

