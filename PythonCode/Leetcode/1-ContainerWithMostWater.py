
'''11. 盛最多水的容器'''
# 每次移动的是左右两个中小的一个索引
def ContainerWithMostWater(height):
    if not height: return 0
    i = 0
    j = len(height)-1
    water = (j-i) * min(height[i], height[j])
    while i < j:
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
        water = max(water, (j-i) * min(height[i], height[j]))
    return water

height = [1,8,6,2,5,4,8,3,7]
print('盛水最多的容器：', ContainerWithMostWater(height))



