# 56. 合并区间

def MergeIntervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0]) # 不一定有序，先排序
    res = [intervals[0]]
    for inter in intervals[1:]:
        if inter[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], inter[1]) # res[-1][1]有可能大于inter[1]
        else:
            res.append(inter)

    return res
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(MergeIntervals(intervals))

