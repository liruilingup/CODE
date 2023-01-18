import sys

s = input()
print(s)

n = len(s)
for i in range(1, n+1):
    for j in range(i, n):
        print('i', s[j:n])


