
'''K个鸡蛋N个楼层'''
def superEggDrop(K,N):
    memo = dict()
    def dp(K,N):
        if N==0:return 0
        if N==1:return 1
        if K==1:return N
        if (K,N) in memo:
            return memo[(K,N)]
        # 二分法穷举 min(max(dp, dp))+1
        res = float('inf')
        low = 0
        hight = N
        while low <= hight:
            mid = (low+hight)//2
            broken = dp(K-1, mid-1)
            not_broken = dp(K, N-mid)
            if broken > not_broken:
                hight = mid-1
                res = min(res, broken+1)
            else:
                low = mid+1
                res = min(res, not_broken+1)
        memo[(K,N)]=res
        return res
    return dp(K,N)

print(superEggDrop(2,10))