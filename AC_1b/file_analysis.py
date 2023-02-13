import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# importing data from lab1_sample.txt
path = "./AC_1b/lab1_sample.txt"
data = np.loadtxt(path)
frequency = data[:,0]
strength = data[:,1]
uncertainty = data[:,2]

frequency_min = np.min(frequency)
frequency_max = np.max(frequency)
frequency_length = np.size(frequency, axis=0)

input = np.linspace(frequency_min, frequency_max, frequency_length)

# gaussian function
def gaussian(input, amplitude, center, deviation):
    return amplitude * np.e ** (-1 * (((input - center) ** 2) / (2 * deviation ** 2)))

# creating a gaussian fit curve (amplitude, center, deviation)
p0 = [0.03, 50, 14]
params, cov = curve_fit(gaussian, input, strength, p0)
y_fit = gaussian(input, params[0], params[1], params[2])
amp = np.around(params[0], 4)
mean = np.around(params[1], 1)
stddev = np.around(params[2], 1)
print("Fit amplitude: ", amp, " Mean: ", mean, " Standard Deviation: ", stddev)

# calculating sigma
sigma = np.sqrt(np.diag(cov))
amp_sigma = np.around(sigma[0], 4)
mean_sigma = np.around(sigma[1], 1)
dev_sigma = np.around(sigma[2], 1)
print("Standard deviations: Amplitude: ", amp_sigma, " Mean: ", mean_sigma, " Standard Deviation: ", dev_sigma)

# plotting data
plt.figure()
plt.errorbar(frequency, strength, yerr = uncertainty, ls = "none", fmt = ".", linewidth = 1)
fitlabel = f"μ = {mean} ± {mean_sigma}\n" + f"Max = {amp} ± {amp_sigma}\n" + f"σ = {stddev} ± {dev_sigma}"
plt.plot(input, y_fit, label = fitlabel)
plt.legend(loc = "upper right")
plt.title("Line Strength by frequency")
plt.xlabel("Frequency")
plt.ylabel("Line Strength")
plt.show()