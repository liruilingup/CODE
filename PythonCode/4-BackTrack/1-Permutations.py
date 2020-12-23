'''全排列问题'''

def Permute(nums) :
    def DfsBacktrack(tmp):
        # 结束条件
        if len(nums) == len(tmp):
            store.append(tmp[:])
        else:
            for i in nums:
                if i in tmp:
                    continue
                tmp.append(i)
                DfsBacktrack(tmp)
                tmp.pop()

    store = []
    tmp = []
    DfsBacktrack(tmp)
    return store
print(Permute([1,2,3]))





'''写法2'''
res = []
def Permution(nums):
    track = []
    DfsTrackBack(nums, track)
    return res

def DfsTrackBack(nums, track):
    if len(track) == len(nums):
        res.append(track[:])
    for num in nums:
        if num in track:
            continue
        track.append(num)
        DfsTrackBack(nums, track)
        track.pop()
nums = [1,2,3]
print('方法2', Permution(nums))
