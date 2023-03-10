import numpy as np
import matplotlib.pyplot as plt

# Dictionary of all temperatures of standards for easy access
# In descending order: O B A F G K M
# --> o5, b0, b6, a1, a5, f0, f5, g0, g6, k0, k5, m0, m5

# Reading in data for unknown 1
unknown1 = np.loadtxt("./BO_AC_3/Unknowns/unknown1.txt")

# Function to plot an unknown and two standards
def plotUnknown(unknownName, highName, lowName):
    plt.figure()
    unknown = np.loadtxt("./BO_AC_3/Unknowns/unknown" + unknownName + ".txt") # importing data from name
    plt.plot(unknown[:,0], unknown[:,1], label="Unknown" + unknownName, color="blue", linestyle="solid")
    high = np.loadtxt("./BO_AC_3/Standards/" + highName + ".txt") # importing data from name
    low = np.loadtxt("./BO_AC_3/Standards/" + lowName + ".txt") # importing data from name
    plt.plot(high[:,0], high[:,1], label=highName, color="orange", linestyle="--")
    plt.plot(low[:,0], low[:,1], label=lowName, color="green", linestyle="--")
    plt.legend()
    plt.title("Unknown" + unknownName + " Compared with Two Standards")
    plt.xlabel("Wavelength (angstroms)")
    plt.ylabel("Intensity (Normalized)")
    plt.show()

def plotResiduals(unknownName, highName, lowName):
    unknown = np.loadtxt("./BO_AC_3/Unknowns/unknown" + unknownName + ".txt") # importing data from name
    high = np.loadtxt("./BO_AC_3/Standards/" + highName + ".txt") # importing data from name
    low = np.loadtxt("./BO_AC_3/Standards/" + lowName + ".txt") # importing data from name
    residual_high = unknown[:,1] - high[:,1] # Residual for one of the two standards
    residual_low = unknown[:,1] - low[:,1] # Residual for the other

    plt.figure()
    plt.plot(unknown[:,0], residual_high, label="Residual with " + highName, color="orange", linestyle="--")
    plt.plot(unknown[:,0], residual_low, label="Residual with " + lowName, color="green", linestyle="--")
    plt.title("Residuals of " + unknownName + " with Two Standards")
    plt.xlabel("Wavelength (angstroms)")
    plt.ylabel("Difference between measured and standard")
    plt.legend()
    plt.show()
    
    sum_squares_high = np.sum(residual_high ** 2) # Finding sum of squares for both standards
    sum_squares_high = np.around(sum_squares_high, 2) # Round to two decimal places
    sum_squares_low = np.sum(residual_low ** 2)
    sum_squares_low = np.around(sum_squares_low, 2)
    print("Sum of squares for unknown" + unknownName + ":") # Printing sum of squares
    print(f"\tSum of squares with ", highName, ": ", sum_squares_high)
    print(f"\tSum of squares with ", lowName, ": ", sum_squares_low)

# Plotting for various standards; manually changing until two match well
# After plotting, plot the residuals and print sum of squares for each

# Unknown1:
plotUnknown("1", "o5", "b0") # Unknown1 is determined to be closest to o5 and b0
plotResiduals("1", "o5", "b0") # o5 is better

# Unknown2:
plotUnknown("2", "m0", "m5") # Unknown2 is determined to be closest to m0 and m5
plotResiduals("2", "m0", "m5") # m0 is better

# Unknown3:
plotUnknown("3", "g6", "k0") # Unknown 3 is determined to be closest to g6 and k0
plotResiduals("3", "g6", "k0") # g6 is better

# Unknown4:
plotUnknown("4", "b6", "a1") # Unknown 4 is determined to be closest to b6 and a1
plotResiduals("4", "b6", "a1") # a1 is better

# Unknown5:
plotUnknown("5", "k5", "m0") # Unknown 5 is determined to be closest to k5 and m0
plotResiduals("5", "k5", "m0") # k5 is better