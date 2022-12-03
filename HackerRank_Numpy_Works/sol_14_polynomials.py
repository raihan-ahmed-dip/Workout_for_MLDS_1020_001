import numpy as np

p = list(map(float, input().split(' ')))
x = int(input())

n = np.polyval(p, x)
print(n)