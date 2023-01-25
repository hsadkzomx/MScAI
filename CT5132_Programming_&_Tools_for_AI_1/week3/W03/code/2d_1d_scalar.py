import numpy as np

a = np.array([[9, 5, 1], [4, 3, 8], [2, 7, 6]]) # shape (3, 3)
b = np.array([[10], [20], [30]])                # shape (3, 1)
c = np.array([100, 200, 300])                   # shape (3,)
d = 1000                                        # shape ()
q = a + b + c + d                               # shape (3, 3)
print(a)
print(b)
print(c)
print(d)
print(q)
