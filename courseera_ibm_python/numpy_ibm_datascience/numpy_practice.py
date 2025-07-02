import numpy as np
import matplotlib.pyplot as plt

# # Define a 2D NumPy array (2 rows, 3 columns)
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])
#
# print("Array:\n", arr)
#
# # Total number of elements
# print("Size:", arr.size)         # 6 elements total (2x3)
#
# # Shape (rows, columns)
# print("Shape:", arr.shape)       # (2, 3)
#
# # Number of dimensions
# print("Dimensions (ndim):", arr.ndim)  # 2D array → ndim = 2
#
# # Length of the array (size of first axis)
# print("Length (len):", len(arr)) # 2 → number of rows

# Define two Python lists (not NumPy arrays)
# u = [1, 0]  # Vector u represents the x-axis unit vector
# v = [0, 1]  # Vector v represents the y-axis unit vector
#
# z = []  # Initialize an empty list to store the result
#
# # Use zip to iterate over pairs of elements from u and v
# for n, m in zip(u, v):
#     z.append(n + m)  # Add corresponding elements from u and v, then append the sum to list z
#
# # Print the resulting list
# print(z)  # Output: [1, 1]
#---------------------------------------------------------------------------------------------------------
# Define two 1-dimensional arrays (vectors)
# u = np.array([1, 0])  # Vector u represents the x-axis unit vector
# v = np.array([0, 1])  # Vector v represents the y-axis unit vector
# type(v) # will give numpy.ndarray
# v.dtype # will give dtype('int32')
# # Perform element-wise addition of vectors u and v
# z = u + v  # This adds corresponding elements: [1+0, 0+1] -> [1, 1]
#
# # Print the result
# print(z)  # Output: [1 1]
#---------------------------------------------------------------------------------------------------------
# # Define two Python lists (not NumPy arrays)
# u = [1, 0]  # Vector u represents the x-axis unit vector
# v = [0, 1]  # Vector v represents the y-axis unit vector
#
# z = []  # Initialize an empty list to store the result
#
# # Use zip to iterate over pairs of elements from u and v
# for n, m in zip(u, v):
#     z.append(n - m)  # Subtract corresponding elements: [1 - 0, 0 - 1] -> append results to list z
#
# # Print the resulting list
# print(z)  # Output: [1, -1]

#---------------------------------------------------------------------------------------------------------
# # Define two 1-dimensional NumPy arrays (vectors)
# u = np.array([1, 0])  # Vector u represents the x-axis unit vector
# v = np.array([0, 1])  # Vector v represents the y-axis unit vector
#
# # Perform element-wise subtraction of vectors u and v
# z = u - v  # Subtract corresponding elements: [1 - 0, 0 - 1] -> [1, -1]
#
# # Print the result
# print(z)  # Output: [ 1 -1 ]

#---------------------------------------------------------------------------------------------------------

# # Define a vector as a Python list
# u = [1, 2, 3]  # Example vector
# scalar = 4     # Scalar value to multiply each element by
#
# # Initialize an empty list for the result
# z = []
#
# # Loop through each element in the vector and multiply by the scalar
# for n in u:
#     z.append(n * scalar)  # Multiply and append to result list
#
# # Print the resulting vector
# print(z)  # Output: [4, 8, 12]
#---------------------------------------------------------------------------------------------------------

# # Define a NumPy array (vector)
# u = np.array([1, 2, 3])  # Example vector
# scalar = 4               # Scalar value to multiply each element by
#
# # Perform element-wise scalar multiplication
# z = scalar * u  # or u * scalar, both are valid
#
# # Print the resulting array
# print(z)  # Output: [ 4  8 12 ]
#---------------------------------------------------------------------------------------------------------
# # Product of two numpy arrays
# # Define two vectors as Python lists
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# # Initialize an empty list to store the result
# product = []
#
# # Perform element-wise multiplication using a loop
# for x, y in zip(a, b):
#     product.append(x * y)  # Multiply corresponding elements and append
#
# # Print the result
# print(product)  # Output: [4, 10, 18]
#---------------------------------------------------------------------------------------------------------
# import numpy as np  # Import NumPy
#
# # Define two vectors as NumPy arrays
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
#
# # Perform element-wise multiplication
# product = a * b  # Multiplies each element at the same index
#
# # Print the result
# print(product)  # Output: [ 4 10 18 ]
#---------------------------------------------------------------------------------------------------------
# dot product in python
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# dot = 0
# for x, y in zip(a, b):
#     dot += x * y
#
# print(dot)  # Output: 32
#---------------------------------------------------------------------------------------------------------
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
#
# dot = np.dot(a, b)
# print(dot)  # Output: 32
#---------------------------------------------------------------------------------------------------------
"""
For two arrays to be broadcastable:

Start from the trailing dimensions (i.e., from the end)

Dimensions must either:

Be equal, or

One of them must be 1

"""
#broadcasting in numpy
#-----------------------------------------------
#adding scalar or constant to numpy array
# a = np.array([1, 2, 3])        # Shape: (3,)
# b = 5                          # Scalar: treated as shape (1,)
#
# result = a + b                 # Adds 5 to each element in a
# # b (scalar) is broadcast to match the shape of a: [5, 5, 5]
# print(result)  # Output: [6 7 8]
# #-----------------------------------------------
# # ✅ 2D + 1D Example
# a = np.array([[1, 2, 3],
#               [4, 5, 6]])       # Shape: (2, 3)
#
# b = np.array([10, 20, 30])      # Shape: (3,)
#
# result = a + b
# print(result)
# # b is broadcast to each row of a
#-----------------------------------------------
# #✅ 2D + column vector (reshape to broadcast along columns)
# a = np.array([[1, 2, 3],
#               [4, 5, 6]])       # Shape: (2, 3)
#
# b = np.array([10, 20]).reshape(2, 1)  # Shape: (2, 1)
#
# result = a + b
# print(result)
# #b is broadcast along the columns to match shape (2, 3)
#---------------------------------------------------------------------------------------------------------

"""
✅ What Are Universal Functions (ufuncs) in NumPy?
Ufuncs are vectorized functions — they operate element-wise on arrays.

They are implemented in C under the hood → very fast.

Ufuncs support broadcasting, type casting, and optional output arrays.

"""
#-----------------------------------------------
# #Arithmetic Ufuncs
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
#
# print(np.add(a, b))      # [5 7 9]
# print(np.subtract(a, b)) # [-3 -3 -3]
# print(np.multiply(a, b)) # [4 10 18]
# print(np.divide(b, a))   # [4.0 2.5 2.0]
# print(np.power(a, 2))    # [1 4 9]

#-----------------------------------------------
# # Trigonometric Ufuncs
# x = np.linspace(0, np.pi, 4)
# print(np.sin(x))  # [0.         0.70710678 1.         0.70710678]
# print(np.cos(x))  # [ 1.000000e+00  7.071068e-01  6.123234e-17 -7.071068e-01]
#-----------------------------------------------
# # Exponential and Logarithmic Ufuncs
# x = np.array([1, np.e, np.e**2])
# print(np.log(x))     # [0. 1. 2.]
# print(np.exp([0, 1, 2]))  # [1.         2.71828183 7.3890561 ]
#-----------------------------------------------
# # Comparison Ufuncs
# a = np.array([1, 2, 3])
# b = np.array([2, 2, 2])
# print(np.greater(a, b))   # [False False  True]
# print(np.equal(a, b))     # [False  True False]
#-----------------------------------------------
# # Rounding and Absolute
# x = np.array([-1.7, -0.2, 3.2, 1.5])
# print(np.abs(x))        # [1.7 0.2 3.2 1.5]
# print(np.floor(x))      # [-2. -1.  3.  1.]
# print(np.ceil(x))       # [-1. -0.  4.  2.]
#-----------------------------------------------
"""
 Are np.mean() and np.max() Ufuncs?
❌ No, technically np.mean(), np.sum(), np.max(), etc., are not ufuncs.

They are aggregation functions (also called reduction operations).

They operate on entire arrays or axes, not element-wise.
"""
# a = np.array([[1, 2], [3, 4]])
#
# print(np.mean(a))      # 2.5 → average of all elements
# print(np.max(a))       # 4   → maximum value
# print(np.sum(a, axis=0))  # [4 6] → column-wise sum
#---------------------------------------------------------------------------------------------------------
"""
np.linspace() – Generate evenly spaced numbers

📌 Syntax: np.linspace(start, stop, num)

start: starting value
stop: ending value
num: how many points to generate (default = 50)
"""
# x = np.linspace(0, 2 * np.pi, 5)  # 100 points from 0 to 2π
# print(x)
#---------------------------------------------------------------------------------------------------------
# # Plotting a sine function using linspace
# # Generate 100 points between 0 and 2π
# x = np.linspace(0, 2 * np.pi, 100)
#
# # Apply sine function to each point
# y = np.sin(x)
#
# # Plot the result
# plt.plot(x, y, label='sin(x)')
# plt.title("Sine Function")
# plt.xlabel("x")
# plt.ylabel("sin(x)")
# plt.grid(True)
# plt.legend()
# plt.show()