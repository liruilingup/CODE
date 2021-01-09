def dicesProbability( n):
    def diceCnt(n):
        if n == 1:
            return [0] + [1] * 6
        cnts = diceCnt(n - 1) + [0] * 6
        for i in range(6 * n, 0, -1):
            cnts[i] = sum(cnts[max(i - 6, 0): i])
        return cnts

    return filter(lambda a: a != 0, list(map(lambda a: a / 6 ** n, diceCnt(n))))
