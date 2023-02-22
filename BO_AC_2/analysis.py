import numpy as np
import matplotlib.pyplot as plt

# Creating array of measured apparent distances (in order datasets 1-10) and uncertainty
a = [9.2, 23.8, 11.3, 16.4, 10.3, 25.0, 12.5, 25.1, 9.2, 21.9]
a = np.array(a)
sigma_a = [1.1, 1.1, 2.1, 1.1, 3.0, 1.1, 1.1, 1.1, 2.1, 1.1]
sigma_a = np.array(sigma_a)

# Creating array of measured plate scales and uncertainty (in order datasets 1-10) and uncertainty
s = [0.051724, 0.004545, 0.003731, 0.061538, 0.058824, 0.008000, 0.109091, 0.003175,0.102564, 0.005405]
s = np.array(s)
sigma_s = [0.000631, 0.000073, 0.000020, 0.000669, 0.000489, 0.000113, 0.001403, 0.000036, 0.001860, 0.000052]
sigma_s = np.array(sigma_s)

# Function to return parallax, parallax uncertainty, distance, and distance uncertainty
# based on values of a, s, and their uncertainties.
# the value of p depends on a and s, the value of p's uncertainty depends on p, a, s, and a/s uncertainties,
# the value of d depends on p, and the value of d uncertainty depends on d, p, and p uncertainty.
def calc_p_d_sigma(a, sigma_a, s, sigma_s):
    p = (a * s) / 2
    sigma_p = p * np.sqrt((sigma_a / a) ** 2 + (sigma_s / s) ** 2)
    d = 1 / p
    sigma_d = (d * sigma_p) / p
    return p, sigma_p, d, sigma_d

# calculating p, sigma_p, d, and sigma_d for dataset 1
p, sigma_p, d, sigma_d = calc_p_d_sigma(a, sigma_a, s, sigma_s)
print("Results for first dataset: ")
print(f"Parallax: (arcsec) ", p[0], ", Uncertainty: ", sigma_p[0], "\nDistance: (parsec) ", d[0], ", Uncertainty: ", sigma_d[0])

# Calculating difference between this data and Hipparcos data
hipparcos = [4.514, 18.4849, 50.5454, 1.9485, 3.182, 4.953, 1.417, 25.143, 2.394, 17.976]
hipparcos = np.array(hipparcos)
difference = d - hipparcos

# Plotting difference between this data and Hipparcos data
plt.figure()
plt.errorbar(np.arange(1, 11), difference, yerr = sigma_d, ls = "none", fmt = ".", linewidth = 1)
plt.xlabel("Dataset")
plt.ylabel("Difference Between Distances (pc)")
plt.title("Measured Star Distances Compared to Distances as Measured by Hipparcos")
plt.show()