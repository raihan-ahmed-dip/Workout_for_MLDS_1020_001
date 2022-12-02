import numpy as np

n, m = map(int, input().split())
l = []
for j in range(n):
    l.append(list(map(int, input().split())))

na = np.array(l)
print(np.max(np.min(na, axis=1)))