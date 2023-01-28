
nums = [5, 2, 8, 4, 7, 4, 3, 9, 2, 0, 16,1]

def bubble(nums):
    nums = [5, 2, 8, 4, 7, 4, 3, 9, 2, 0, 16, 1]
    lens = len(nums)
    for i in range(lens):
        for j in range(i, lens):
            print(lens[j])

if __name__ == "__main__":
    bubble(nums)

