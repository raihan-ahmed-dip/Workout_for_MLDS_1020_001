import numpy as np

n, m = map(int, input().split())

lst = []

for i in range(n):
    lm = list(map(int, input().split()))
    lst.append(lm)

nma = np.array(lst)
print(np.prod(np.sum(nma, axis=0)))
