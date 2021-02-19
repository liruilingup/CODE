import heapq

'''
维护一个最大堆，一个最小堆
    最大堆存储数据流中 值较小的一半元素
    最小堆存储数据流中 值较大的一半元素
    若总元素个数为奇数，则最大堆比最小堆多放一个元素

如何实现两个堆的元素数量平衡？
    首先将元素添加到最大堆中
    将最大堆中最大的元素移到最小堆中
    如果最小堆元素个数比最大堆多，则将最小堆中最小元素移到最大堆中
数据流的中位数：
    要么是两个堆的堆顶元素，要么是最大堆的堆顶元素


'''
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):# 先加到大顶堆，再把大堆顶元素加到小顶堆
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:  # 先加到小顶堆，再把小堆顶元素加到大顶堆
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]

