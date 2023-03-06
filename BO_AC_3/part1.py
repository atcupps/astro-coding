import numpy as np
import matplotlib.pyplot as plt

# Function for Planck's Law in SI units
# Speed of light c = 299 792 458 m / s
# Planck's constant h = 6.62607015 x 10^(-34)
# Boltzmann constant k_B = 1.380649 x 10^(-23)
c = 299792458
h = 6.62607015 * (10 ** (-34))
kB = 1.380649 * (10 ** (-23))
def planck(wavelength, temperature):
    left = (2 * h * (c ** 2)) / (wavelength ** 5)
    right = 1 / (np.exp((h * c) / (wavelength * kB * temperature)) - 1)
    return left * right

# Creating an array of wavelengths from 10^(-10)m to 1.5 * 10^(-6) m
wavelengths = np.linspace(10 ** (-10), 1.5 * (10 ** (-6)), 100)

# A0 temp = 9600 K; Sun, Sun temp = 5800 K; M0, M0 temp = 3750 K
A0 = planck(wavelengths, 9600) # Curve for A0
Sun = planck(wavelengths, 5800) # Curve for the Sun
M0 = planck(wavelengths, 3750) # Curve for M0

# Plotting the curves for A0, the Sun, and M0
plt.figure()
plt.plot(wavelengths, A0, label = "A0", color = "blue", linestyle = "solid") # 
plt.plot(wavelengths, Sun, label = "Sun", color = "gold", linestyle = "--")
plt.plot(wavelengths, M0, label = "M0", color = "red", linestyle = ":")
plt.title("Theoretical Intensity Curve for Various Stars")
plt.xlabel("Wavelength (m)")
plt.ylabel("Intensity (W sr^-1 m^-3)")
plt.legend()
plt.show()

# Reading in the data for a B0 star (B0 temp is 29200 K)
B0_real = np.loadtxt("./BO_AC_3/Standards/b0.txt")

# Generating theoretical data for a B0 star from 3900 Ang. to 4500 Ang
# 1 angstrom = 10^(-10) m

# Function to convert to m
def toMeters(angstroms):
    return angstroms * 10 ** (-10)

# Range of angstroms from 3900 to 4500
angstroms = np.linspace(3900, 4500, 500)
angToM = toMeters(angstroms)
B0_sim_intensities = planck(angToM, 29200)
B0_normalized = B0_sim_intensities / np.max(B0_sim_intensities)

# Plotting the real vs. simulated curves for B0
plt.figure()
plt.plot(B0_real[:,0], B0_real[:,1], label="Real", linestyle="solid")
plt.plot(angstroms, B0_normalized, label="Simulated", linestyle="--")
plt.title("Theoretical vs. Observed Curve for a B0 Star")
plt.xlabel("Wavelength (angstrom)")
plt.ylabel("Intensity (normalized ratio)")
plt.legend()
plt.show()