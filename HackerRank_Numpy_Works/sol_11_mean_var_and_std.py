import numpy as np

n, m = map(int, input().split())
l = []
for j in range(n):
    l.append(list(map(int, input().split())))
    
na = np.array(l)
print(np.mean(na, axis=1))      # Mean
print(np.var(na, axis=0))       # Variance
print(round(np.std(na), 11))    # Standard Deviation