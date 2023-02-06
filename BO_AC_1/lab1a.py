import numpy as np
import matplotlib.pyplot as plt

# Question 3
arr = [[1, 2, 3, 2, 4, 6, 3, 6, 9], [4, 5, 6, 8, 10, 12, 12, 15, 18]]
arr = np.array(arr)

# Question 4
B = np.arange(0, 10, 2)
A = np.array([np.zeros(5), B])
S = A.shape
Q = S[0] + len(B) - A[1, 3] + (np.zeros((2, 3))).size

# Question 5
r = np.random.rand(8)
r = np.sort(r)
print(r)
mean = np.mean(r)
print(mean)

# Question 6

# This function takes an input, x, and returns the value of
# the square root of (x^2 + 15).
def y(x):
    return np.sqrt(x ** 2 + 15)

# example using y evaluated for x = 5
print("f(5): " + str(y(5)))

# Question 7

# parts a-e
a = np.array([[1, 4, 7], [3, 5, 8]]) # 2d array of 1, 4, 7 and 3, 5, 8
b = np.arange(10, 50, 0.1) # array from 10 to 50 by intervals of 0.1
c = np.linspace(10, 50, 1900) # array with 1900 evenly-spaced points from 10 to 50
d = 5 * np.cos(b) # array of 5 times cosine of the array in part b
e = 3 * c # array of 3 times the resulting array from part c

# part f
plt.figure()
plt.plot(b, d, color="blue", linestyle="solid") # solution to part d
plt.plot(c, e, color="black", linestyle="dashed") # solution to part e
plt.title("y = 5cos(x) compared to y = 3x") # title
plt.xlabel("x from 10 to 50") # xlabel
plt.ylabel("5cos(x) (solid) and 3x (dashed)")
plt.show()

# part g
g = y(b)

# part h
plt.figure()
plt.plot(b, g) # plot y(x) as defined earlier by the function y(x)
plt.gca().invert_xaxis() # invert x axis
plt.title("y(x) from 50 to 10") # title
plt.xlabel("x from 50 to 10") # x label
plt.ylabel("y(x) = sqrt(x^2 + 15)") # y label
plt.show()