import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Reading in data after calculating in excel spreadsheet
data = np.loadtxt("data.fred")
distances = data[:,0]
sigma_dist = data[:,1]
velocities = data[:,2]
sigma_v = data[:,3]

# Finding line of best fit for a non-zero intercept
def line_unbound(x, a, b):
    return a*x + b
popt_ub, pcov_ub = curve_fit(line_unbound, distances, velocities)
sigma_fit_ub = np.sqrt(np.diag(pcov_ub))

# Finding line of best fit for a zero intercept
def line_bound(x, a):
    return a*x
popt_b, pcov_b = curve_fit(line_bound, distances, velocities)
sigma_fit_b = np.sqrt(np.diag(pcov_b))


# Plotting
plt.figure()

# Modified distances to include 0
distances_modified = np.append(distances, 0)

# Drawing line of best fit
plt.plot(distances_modified, line_unbound(distances_modified, *popt_ub), color="red", label="Non-zero intercept:\n" + r'$H_0 = $' + str(popt_ub[0])[0:4] + r'$\pm$' + str(sigma_fit_ub[0])[0:3] + "\n" + r'$v(0) = $' + str(popt_ub[1])[0:4] + r'$\pm$' + str(sigma_fit_ub[1])[0:5])
plt.plot(distances_modified, line_bound(distances_modified, *popt_b), color="blue", label="Zero intercept:\n" + r'$H_0 = $' + str(popt_b[0])[0:4] + r'$\pm$' + str(sigma_fit_b[0])[0:3])

# Plotting data with error bars
plt.errorbar(x=distances, y=velocities, xerr=sigma_dist, yerr=sigma_v, ls="none", capsize=2, color="black", elinewidth=1)
plt.scatter(x=distances, y=velocities, s=9, color="black")

plt.xlabel("d = Distance away (Mpc)")
plt.ylabel("v = Recessional velocity (km/s)")
plt.title("Velocity of galaxies at different distances based on redshift")
plt.legend()

plt.savefig("hubble_plot.png", dpi=300)
plt.show()