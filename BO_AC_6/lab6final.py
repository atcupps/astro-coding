import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Reading in data after calculating in excel spreadsheet
data = np.loadtxt("data.fred")
distances = data[:,0]
sigma_dist = data[:,1]
velocities = data[:,2]
sigma_v = data[:,3]

# Finding line of best fit
def line(x, a, b):
    return a*x + b
popt, pcov = curve_fit(line, distances, velocities)
sigma_fit = np.sqrt(np.diag(pcov))

# Plotting
plt.figure()

# Drawing line of best fit
plt.plot(distances, line(distances, *popt), color="red", label=r'$v=H_0d$' + "\n" + r'$H_0 = $' + str(popt[0])[0:4] + r'$\pm$' + str(sigma_fit[0])[0:3] + "\n" + r'$v(0) = $' + str(popt[1])[0:4] + r'$\pm$' + str(sigma_fit[1])[0:5])

# Plotting data with error bars
plt.errorbar(x=distances, y=velocities, xerr=sigma_dist, yerr=sigma_v, ls="none", capsize=2, color="black", elinewidth=1)
plt.scatter(x=distances, y=velocities, s=9, color="black")

plt.xlabel("d = Distance away (Mpc)")
plt.ylabel("v = Recessional velocity (km/s)")
plt.title("Velocity of galaxies at different distances based on redshift")
plt.legend()

plt.savefig("hubble_plot.png", dpi=300)
plt.show()