import pandas
import numpy as np
import matplotlib.pyplot as plt

# filepaths for m45, and m67 data
m45_path = "BO_AC_4/m45.txt"
m67_path = "BO_AC_4/m67.txt"

# using pandas to read in only the B and V columns of m45 and m67
m45 = pandas.read_table(m45_path, sep='\t', usecols=[2, 3], na_values='')
m67 = pandas.read_table(m67_path, sep='\t', usecols=[10, 11], na_values='')

# Plotting V as a function of (B - V) for m45
plt.figure()
plt.scatter(m45['B'] - m45['V'], m45['V'], s=[4])
plt.gca().invert_yaxis() # smaller V is brighter
plt.title("CMD Diagram for M45")
plt.xlabel("Color Index Difference of Blue and Visible (B - V)")
plt.ylabel("Apparent Magnitude in Visible Color Index (V)")
plt.show()

# Function for Planck's Law in SI units (from lab 3)
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

# Ballesteros formula for temperature
def temp_from_BV(BV):
    return 4600 * ((1 / (0.92 * BV + 1.7)) + (1 / (0.92 * BV + 0.62)))

# Get temperature of a star with (B-V) of 0.5:
temp1 = temp_from_BV(0.5)
# Creating an array of wavelengths from 10^(-10)m to 1.5 * 10^(-6) m
wavelengths = np.linspace(10 ** (-10), 1.5 * (10 ** (-6)), 100)
# Getting the planck function intensities for (B-V) = 0.5
intensities1 = planck(wavelengths, temp1)

# Getting the temperature of a star with (B-V) of 0.6:
temp2 = temp_from_BV(0.6)
# Getting the planck function intensities for (B-V) = 0.6:
intensities2 = planck(wavelengths, temp2)

# PLOT for blackbody curves and color filter ranges
plt.figure()

# Plotting blackbody curve for a star with (B - V) = 0.5
plt.plot(wavelengths, intensities1, label="(B-V) = 0.5")

# Plotting blackbody curve for a star with (B - V) = 0.6
plt.plot(wavelengths, intensities2, label="(B-V) = 0.6")

# Labels
plt.title("Blackbody Curves for Stars of Different (B-V) Values with B and V Ranges Shown")
plt.xlabel("Wavelength (m)")
plt.ylabel("Intensity (W sr^-1 m^-3)")

'''
Showing regions of wavelengths allowed through by B and V filters

According to https://mcdonaldobservatory.org/research/instruments/ubvri-filters, 
B ranges from 400 to 500 nm, while V ranges from 500 nm to 700 nm.
'''
plt.axvspan(400 * (10 ** (-9)), 500 * (10 ** (-9)), color='blue', alpha = 0.23) # For B
plt.axvspan(500 * (10 ** (-9)), 700 * (10 ** (-9)), color='green', alpha=0.23) # For V

plt.legend()
plt.show()