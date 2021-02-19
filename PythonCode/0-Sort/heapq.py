# Python的heap的使用
import heapq

heap = [1,3,4,2,6,8,9]
# 使数组转化为堆
heapq.heapify(heap)
# 为heap增加元素
heapq.heappush(heap, 2)
# 删除堆顶（即最小值）
heapq.heappop(heap)
# 查堆中最大n个数
print(heapq.nlargest (2, heap))
#查询堆中的最小元素，n表示查询元素个数
print(heapq.nsmallest(3, heap) )

# 将 item 放入堆中，然后弹出并返回 heap 的最小元素
heapq.heappushpop(heap, 10)

print(heap)

