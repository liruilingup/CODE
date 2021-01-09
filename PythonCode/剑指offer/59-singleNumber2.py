def singleNumber(nums):
    ones, twos = 0, 0
    for num in nums:
        ones = ones ^ num & ~twos
        twos = twos ^ num & ~ones
    return ones