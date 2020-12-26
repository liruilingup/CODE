'''sort()与sorted()的不同在于，sort是在原位重新排列列表，而sorted()是产生一个新的列表'''
print('sort()和sorted()函数的区别就是：sort()直接排序，改变原数组；sorted()需要输入数组参数，并且赋值，不改变原来的数组')

'''一维数组的排序'''
nums = [10,9,2,5,3,7,101,18]
nums.sort(reverse=0)
nums.sort(reverse=False)
print('升序', nums)
nums = [10,9,2,5,3,7,101,18]
nums.sort(reverse=-1)
nums.sort(reverse=True)
print('降序', nums)


'''多维数组的排序'''
a = [[2,3,4], [2,4,5],[3,3,4]]
a.sort(key=lambda x: (x[1], -x[0]))
print('多维数组的排序，先按照x[1]升序，再按照x[0]降序：', a)

'''sorted()函数的使用方法'''
nums = [[5,4], [6,4], [6,7], [2,3]]
sort_nums = sorted(nums, key=lambda x: (x[1], -x[0]), reverse=True) # 跟x[1], -x[0]相反
print('1、先按照x[1]升序，再按照x[0]降序，sorted()排序后的数组', sort_nums)
sort_nums = sorted(nums, key=lambda x: (x[1], -x[0]), reverse=False)
print('2、先按照x[1]升序，再按照x[0]降序，sorted()排序后的数组', sort_nums)
sort_nums = sorted(nums, key=lambda x: (x[1], -x[0]))
print('3、先按照x[1]升序，再按照x[0]降序，sorted()排序后的数组', sort_nums)

'''字典的排序'''
dicta = {'a':10, 'd':8, 'c':11}
dict_sort = sorted(dicta.items(), key=lambda x:(x[0]))
print('字典的排序结果', dict_sort)



