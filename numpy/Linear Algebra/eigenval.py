import numpy as np

A = np.array([[1,2],[3,4]])

values, vectors = np.linalg.eig(A)
print("Values: " + str(values))
print("Vectors: " + str(vectors))