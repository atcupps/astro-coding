import pandas
import numpy as np
import matplotlib.pyplot as plt
import json

# filepaths for m45, and m67 data
m45_path = "BO_AC_4/m45.txt"
m67_path = "BO_AC_4/m67.txt"

# using pandas to read in only the B and V columns of m45 and m67
m45 = pandas.read_table(m45_path, sep='\t', usecols=[2, 3], na_values=['', ' '])
m67 = pandas.read_table(m67_path, sep='\t', usecols=[10, 11], na_values=['', ' '])

# filepath for isochrones
isochrones_path = "BO_AC_4/isochrones.json"

# reading in data for isochrones into a dictionary
with open(isochrones_path, 'r') as f:
    isochrones = json.load(f)

# A function to plot an isochrone given its data
def plot_isoc(b_abs, v_abs, label_in, distance):
    # Using the distance modulus formula:
    b_app = 5*np.log10(distance) - 5 + b_abs
    v_app = 5*np.log10(distance) - 5 + v_abs
    plt.plot(b_app - v_app, v_app, label=label_in, alpha=0.7)

# Plot for Isochrones
plt.figure()

distance1 = 40 # parsecs

# Getting data for stars of age 5e9
age5e9 = isochrones['e9']['five']
age5e9_B = np.array(age5e9['B'])
age5e9_V = np.array(age5e9['V'])

# Plotting isochrone for stars of age 5e9
plot_isoc(age5e9_B, age5e9_V, "5 x 10^9 years", distance1)

# Getting data for stars of age 9.5e9
age9p5e9 = isochrones['e9']['ninept5']
age9p5e9_B = np.array(age9p5e9['B'])
age9p5e9_V = np.array(age9p5e9['V'])

# Plotting isochrone for stars of age 9.5e9
plot_isoc(age9p5e9_B, age9p5e9_V, "9.5 x 10^9 years", distance1)

# Getting data for stars of age 2e8
age2e8 = isochrones['e8']['two']
age2e8_B = np.array(age2e8['B'])
age2e8_V = np.array(age2e8['V'])

# Plotting isochrone for stars of age 2e8
plot_isoc(age2e8_B, age2e8_V, "2 x 10^8 years", distance1)

# Getting data for stars of age 7e8
age7e8 = isochrones['e8']['seven']
age7e8_B = np.array(age7e8['B'])
age7e8_V = np.array(age7e8['V'])

# Plotting isochrone for stars of age 7e8
plot_isoc(age7e8_B, age7e8_V, "7 x 10^8 years", distance1)


plt.gca().invert_yaxis() # smaller V is brighter
plt.title("CMD for Isochrones at 40 pc")
plt.xlabel("Color Index Difference of Blue and Visible (B - V)")
plt.ylabel("Absolute Magnitude in Visible Color Index (V)")

plt.legend()
plt.gcf().savefig(fname="BO_AC_4/images/Isochrones_40pc.png", dpi=300)
plt.show()

# PLOT FOR M45 WITH MULTIPLE ISOCHRONES:

plt.figure()

# Distance for M45 (found through guess and check aligning the main sequence):
distance_m45 = 132.5 # uncertainty of 7.5

# Scatter plot for data for M45
plt.scatter(m45['B'] - m45['V'], m45['V'], s=[4], label="M45", alpha=0.44, color="orange")

# Age for M45 (found through guess and check aligning turn-off point):
m45iso = isochrones['e8']['one']
m45iso_B = np.array(m45iso['B'])
m45iso_V = np.array(m45iso['V'])
plot_isoc(m45iso_B, m45iso_V, "1 x 10^8 years", distance_m45)

plot_isoc(age2e8_B, age2e8_V, "2 x 10^8 years", distance_m45)

m45iso = isochrones['e8']['three']
m45iso_B = np.array(m45iso['B'])
m45iso_V = np.array(m45iso['V'])
plot_isoc(m45iso_B, m45iso_V, "3 x 10^8 years", distance_m45)


plt.gca().invert_yaxis() # smaller V is brighter
plt.title("Comparison of Reasonable Isochrone Ages to M45")
plt.xlabel("Color Index Difference of Blue and Visible (B - V)")
plt.ylabel("Apparent Magnitude in Visible Color Index (V)")

plt.legend()
plt.gcf().savefig(fname="BO_AC_4/images/M45_Multiple.png", dpi=300)
plt.show()

# PLOT FOR M45 COMPARING DISTANCES:

plt.figure()

# Scatter plot for data for M45
plt.scatter(m45['B'] - m45['V'], m45['V'], s=[4], label="M45", alpha=0.44, color="orange")


# Distance for M45:
distance_m45 = 125

# Age for M45 (found through guess and check aligning turn-off point):
plot_isoc(age2e8_B, age2e8_V, "125 pc", distance_m45)

distance_m45 = 132.5

# Age for M45 (found through guess and check aligning turn-off point):
plot_isoc(age2e8_B, age2e8_V, "132.5 pc", distance_m45)

distance_m45 = 140

# Age for M45 (found through guess and check aligning turn-off point):
plot_isoc(age2e8_B, age2e8_V, "140 pc", distance_m45)


plt.gca().invert_yaxis() # smaller V is brighter
plt.title("Comparison of Reasonable Distances for M45")
plt.xlabel("Color Index Difference of Blue and Visible (B - V)")
plt.ylabel("Apparent Magnitude in Visible Color Index (V)")

plt.legend()
plt.gcf().savefig(fname="BO_AC_4/images/M45_Distances.png", dpi=300)
plt.show()

# FINAL PLOT FOR M45:

plt.figure()

# Distance for M45 (found through guess and check aligning the main sequence):
distance_m45 = 132.5 # uncertainty of 7.5

# Scatter plot for data for M45
plt.scatter(m45['B'] - m45['V'], m45['V'], s=[4], label="M45", alpha=0.44, color="orange")

# Age for M45 (found through guess and check aligning turn-off point):
plot_isoc(age2e8_B, age2e8_V, "2 x 10^8 years, 132.5 pc", distance_m45)


plt.gca().invert_yaxis() # smaller V is brighter
plt.title("CMD for M45 and Isochrone")
plt.xlabel("Color Index Difference of Blue and Visible (B - V)")
plt.ylabel("Apparent Magnitude in Visible Color Index (V)")

plt.legend()
plt.gcf().savefig(fname="BO_AC_4/images/M45_Fit.png", dpi=300)
plt.show()

# PLOT FOR M67 WITH MULTIPLE ISOCHRONES:

plt.figure()

# Distance for M67 (found through guess and check aligning the main sequence):
distance_m67 = 850 # uncertainty of +/- 100 parsecs

# Scatter plot for data for M67
plt.scatter(m67['B'] - m67['V'], m67['V'], s=[4], label="M67", alpha=0.33, color="orange")

# Age for M67 (found through guess and check aligning turn-off point): uncertainty of +/- 5 x 10^8 years
m67iso = isochrones['e9']['two']
m67iso_B = np.array(m67iso['B'])
m67iso_V = np.array(m67iso['V'])
plot_isoc(m67iso_B, m67iso_V, "2 x 10^9 years", distance_m67)

m67iso = isochrones['e9']['three']
m67iso_B = np.array(m67iso['B'])
m67iso_V = np.array(m67iso['V'])
plot_isoc(m67iso_B, m67iso_V, "3 x 10^9 years", distance_m67)

m67iso = isochrones['e9']['four']
m67iso_B = np.array(m67iso['B'])
m67iso_V = np.array(m67iso['V'])
plot_isoc(m67iso_B, m67iso_V, "4 x 10^9 years", distance_m67)

plt.gca().invert_yaxis() # smaller V is brighter
plt.title("Comparison of Reasonable Isochrone Ages for M67")
plt.xlabel("Color Index Difference of Blue and Visible (B - V)")
plt.ylabel("Apparent Magnitude in Visible Color Index (V)")

plt.legend()
plt.gcf().savefig(fname="BO_AC_4/images/M67_Multiple.png", dpi=300)
plt.show()

# PLOT FOR M67 WITH DIFFERENT AGES:

plt.figure()

# Scatter plot for data for M67
plt.scatter(m67['B'] - m67['V'], m67['V'], s=[4], label="M67", alpha=0.33, color="orange")

# Age for M67 (found through guess and check aligning turn-off point): uncertainty of +/- 5 x 10^8 years
m67iso = isochrones['e9']['three']
m67iso_B = np.array(m67iso['B'])
m67iso_V = np.array(m67iso['V'])

distance_m67 = 750
plot_isoc(m67iso_B, m67iso_V, "750 pc", distance_m67)

distance_m67 = 850
plot_isoc(m67iso_B, m67iso_V, "850 pc", distance_m67)

distance_m67 = 950
plot_isoc(m67iso_B, m67iso_V, "950 pc", distance_m67)

plt.gca().invert_yaxis() # smaller V is brighter
plt.title("Comparison of Reasonable Distances for M67")
plt.xlabel("Color Index Difference of Blue and Visible (B - V)")
plt.ylabel("Apparent Magnitude in Visible Color Index (V)")

plt.legend()
plt.gcf().savefig(fname="BO_AC_4/images/M67_Distances.png", dpi=300)
plt.show()

# FINAL PLOT FOR M67:

plt.figure()

# Distance for M67 (found through guess and check aligning the main sequence):
distance_m67 = 850 # uncertainty of +/- 100 parsecs

# Scatter plot for data for M67
plt.scatter(m67['B'] - m67['V'], m67['V'], s=[4], label="M67", alpha=0.33, color="orange")

# Age for M67 (found through guess and check aligning turn-off point): uncertainty of +/- 5 x 10^8 years
m67iso = isochrones['e9']['three']
m67iso_B = np.array(m67iso['B'])
m67iso_V = np.array(m67iso['V'])
plot_isoc(m67iso_B, m67iso_V, "3 x 10^9 years, 850 pc ", distance_m67)

plt.gca().invert_yaxis() # smaller V is brighter
plt.title("CMD for M67 and Isochrone")
plt.xlabel("Color Index Difference of Blue and Visible (B - V)")
plt.ylabel("Apparent Magnitude in Visible Color Index (V)")

plt.legend()
plt.gcf().savefig(fname="BO_AC_4/images/M67_Fit.png", dpi=300)
plt.show()