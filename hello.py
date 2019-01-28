import numpy as np

# Vector
x = np.array((1, 2, 3))
print(x)
print("Vector Dimensions: {}".format(x.shape))
print("Vector Size: {}".format(x.size))

# Matrix
y = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(y)
print("Matrix Dimensions: {}".format(y.shape))
print("Matrix Size: {}".format(y.size))

# define a matrix of a given dimension
z = np.ones((9, 9))
print(z)
print("Matrix Dimensions: {}".format(z.shape))
print("Matrix Size: {}".format(z.size))

a = np.ones((3, 3, 3, 3))
print(a)
print("Tensor Dimensions: {}".format(a.shape))
print("Tensor Size: {}".format(a.size))

# indexing
A = np.ones((5, 5), dtype=np.int)
print(A)

# indexing starts at _
A[0, 2] = 2
A[1, 1] = 9
print(A)

# init all column
A[:, 4] = 8
print(A)

# for higher dimensions, simply add and index
B = np.ones((5, 5, 5), dtype=np.int)

# assign first row a new value
B[:, 0, 0] = 6
print(B)
print("-------------")

# matrix operations
X = np.matrix([[1, 2], [3, 4]])
Y = np.ones((2, 2), dtype=np.int)
print("Matrix X")
print(X)
print("Matrix Y")
print(Y)
Z = X + Y
print("Hasil Z = X + Y")
print(Z)