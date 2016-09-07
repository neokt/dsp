# Matrix Algebra
import numpy as np

A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([[6, 2, -3, 5]])
v = np.array([[3, 5, -1, 4]])
w = np.array([[1], [8], [0], [5]])

# 1. Matrix Dimensions
# 1.1) (2, 3)
# 1.2) (2, 2)
# 1.3) (3, 2)
# 1.4) (2, 3)
# 1.5) (1, 4)
# 1.6) (4, 1)

print "1. Matrix Dimensions"
print "1.1)", A.shape
print "1.2)", B.shape
print "1.3)", C.shape
print "1.4)", D.shape
print "1.5)", u.shape
print "1.6)", w.shape

# 2. Vector Operations
# 2.1) [[ 9  7 -4  9]]
# 2.2) [[ 3 -3 -2  1]]
# 2.3) [[ 36  12 -18  30]]
# 2.4) [[51]]
# 2.5) 8.60232526704

print "\n2. Vector Operations"
a = 6
print "2.1)", u + v
print "2.2)", u - v
print "2.3)", a * u
print "2.4)", np.inner(u, v)
print "2.5)", np.linalg.norm(u)

# 3. Matrix Operations
# 3.1) Not defined
# 3.2)
# [[-4 -7 -3]
#  [ 3  6  4]]
# 3.3)
# [[14  3  3]
#  [ 2  7  9]]
# 3.4)
# [[-1 -5 -1]
#  [ 2  7  4]]
# 3.5) Not defined
# 3.6) Not defined
# 3.7)
# [[ 5 -6]
#  [ 9 -8]
#  [ 6 -6]]
# 3.8)
# [[ 1 -4]
#  [ 0  1]]
# 3.9)
# [[14 28]
#  [28 69]]
# 3.10)
# [[10 -4  0]
#  [-4  8  8]
#  [ 0  8 10]]

print "\n3. Matrix Operations"
print "3.1) Not defined"
print "3.2)\n", A - C.transpose()
print "3.3)\n", C.transpose() + 3 * D
print "3.4)\n", np.dot(B, A)
print "3.5) Not defined"
print "3.6) Not defined"
print "3.7)\n", np.dot(C, B)
print "3.8)\n", np.linalg.matrix_power(B, 4)
print "3.9)\n", np.dot(A, A.transpose())
print "3.10)\n", np.dot(D.transpose(), D)