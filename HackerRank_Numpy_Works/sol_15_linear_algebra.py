import numpy as np

n = int(input())
l = []
for i in range(n):
    l.append(list(map(float, input().split())))

a = np.array(l)

print(round(np.linalg.det(a), 2))