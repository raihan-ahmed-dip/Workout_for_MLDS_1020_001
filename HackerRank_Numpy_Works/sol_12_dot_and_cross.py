import numpy as np

n = int(input())

al = []
for i in range(n):
    al.append(list(map(int, input().split())))
a = np.array(al)

bl = []
for i in range(n):
    bl.append(list(map(int, input().split())))

b = np.array(bl)

c = np.dot(a, b)
print(c)