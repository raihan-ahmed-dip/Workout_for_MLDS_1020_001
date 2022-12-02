import numpy as np

n, m , p = map(int, input().split())

la = []
lb = []

for i in range(n):
    la.append(list(map(int, input().split())))
for j in range(m):
    lb.append(list(map(int, input().split())))

na = np.array(la)
nb = np.array(lb)
nc = np.concatenate((na, nb), axis=0)
print(nc)
