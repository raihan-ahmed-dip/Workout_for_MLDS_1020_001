import numpy as np

inp = input().strip().split(' ')
n = np.array(inp, dtype=int)
n = n.reshape(3, 3)
print(n)