def reverseLeftWords(s, n):
    res = ""
    for i in range(n, len(s)):
        res += s[i]
    for i in range(n):
        res += s[i]
    return res
