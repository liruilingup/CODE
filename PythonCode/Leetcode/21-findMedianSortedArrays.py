'''
寻找两个正序数组的中位数
根据中位数的定义：
当m+n是奇数时，中位数是两个有序数组中的第 (m+n)/2 个元素
当 m+n是偶数时，中位数是两个有序数组中的第 (m+n)/2 个元素和第 (m+n)/2+1 个元素的平均值。
因此，这道题可以转化成寻找两个有序数组中的第 k 小的数，其中 k 为 (m+n)/2或 (m+n)/2+1。
一、如果A[k/2−1]<B[k/2−1]，则A[k/2−1] 小的数最多只有A的前k/2-1个数和B的前k/2−1个数，
    即A[k/2−1] 小的数最多只有 k−2 个，因此A[k/2−1]不可能是第 k 个数，A[0] 到 A[k/2−1] 也都不可能是第 k 个数，可以全部排除。
二、如果A[k/2−1]>B[k/2−1]，则可以排除 B[0] 到B[k/2−1]。
三、如果A[k/2−1]=B[k/2−1]，则可以归入第一种情况处理。
'''

def findMedianSortedArrays(nums1, nums2):
    def getKthElement(k):
        index1 = 0
        index2 = 0
        while True:
            if index1 == m:
                return nums2[index2 + k - 1]
            if index2 == n:
                return nums1[index1 + k - 1]
            if k==1:
                return min(nums1[index1], nums2[index2])
            newIndex1 = min(index1 + k//2-1, m-1)
            newIndex2 = min(index2 + k//2-1, n-1)
            pivot1 = nums1[newIndex1]
            pivot2 = nums2[newIndex2]
            print(index1,index2,newIndex1, newIndex2, pivot1, pivot2, m, n)
            if pivot1 <= pivot2:
                k -= newIndex1-index1 + 1
                index1 = newIndex1 + 1
            else:
                k -= newIndex2 - index2 + 1
                index2 = newIndex2 + 1

    m = len(nums1)
    n = len(nums2)
    if (m+n) % 2 == 1:
        return getKthElement((m+n+1)//2)
    else:
        return (getKthElement((m + n) // 2) + getKthElement((m + n) // 2 + 1)) / 2

nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))

