import numpy as np
import matplotlib.pyplot as plt

# text = "Hello world!"

# print(text[1])
# print(text[-3])
# print(text[:3])
# print(text[4:])
# print(text[4:7])

# c = [0,1,2,3,4,5,6,7,8,9]
# c = np.array(c)

# d = c ** 2
# print(d)

# x = np.arange(0, 10, 1)
# y = np.linspace(0, 10, 12)

# # print(x)
# # print(y)

# path = "./astrodata.txt"
# astrodata = [y, y ** 2]
# np.savetxt(path, astrodata)

X = np.linspace(-5, 5, 100)
S = np.sin(X)
C = np.cos(X)

plt.figure()
plt.plot(X, S)
plt.show()