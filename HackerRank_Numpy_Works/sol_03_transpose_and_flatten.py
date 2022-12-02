import numpy as np

n, m = map(int, input().split())
l = []

for i in range(n):
    l.append(list(map(int, input().split())))

na = np.array(l)
print(np.transpose(na))
print(na.flatten())