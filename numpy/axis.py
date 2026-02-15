import numpy as np

mat = np.array([[1, 2, 3],
                [4, 5, 6]])

print(np.sum(mat, axis=0))  # column sum
print(np.sum(mat, axis=1))  # row sum



