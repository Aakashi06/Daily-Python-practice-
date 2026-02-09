import numpy as np

a1 = np.array([1,2,3,4]) #one dim array
a2 = np.array([[1,2,3,4],[5,6,7,8]]) #two dim array

a3 = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]],[[17,18,19,20],[21,22,23,24]]])

print("One Dimensional Array:" ,a1)
print("Two Dimensional Array:" ,a2)
print("Three Dimensional Array:",a3)


print(a1.ndim)
print(a2.ndim)
print(a3.ndim)



print("Parameters of a1:")
print(a1.shape)
print(a1.size)
print(a1.dtype)


print("Parameters of a2:")
print(a2.shape)
print(a2.size)
print(a2.dtype)


print("Parameters of a3:")
print(a3.shape)
print(a3.size)
print(a3.dtype)