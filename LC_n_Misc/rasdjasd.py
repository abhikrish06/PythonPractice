import numpy as np
a = np.random.randn(3,4,1)
b = np.random.randn(3,1,2)
c = np.random.randn(3,1,1)

d = c + a*b
print(d.shape)

print('c'.islower())
print('('.islower())
print('2'.islower())

