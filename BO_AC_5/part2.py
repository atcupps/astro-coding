import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Function to load the data based on the number galactic longitude
def load_lon(num):
    return np.loadtxt("./Lon-data/lon" + str(num) + ".dat")

'''
Function to find where a signal begins;
the frequency at which a signal begins is determined to be the frequency where the signal first exceeds 5 K.
Since it is unlikely for any given data to have such a point where the signal is exactly 5 K, this function
returns the average of the last frequency where the signal is less than 5 K and the first frequency where the signal exceeds 5 K.
This function returns these two values in that order (last freq < 5K, first freq > 5K)
This method results in an error equal to +/- half the difference of these two values.
'''
threshold = 15
def find_first_signal(data):
    i = 1
    while (data[i,1] < threshold):
        i = i + 1
    return data[i-1,0], data[i,0]

lon17 = load_lon(17) # Loading the longitude 17 data
lon17_freq_before, lon17_freq_after = find_first_signal(lon17) # Find beginning of first signal
lon17_freq = (lon17_freq_before + lon17_freq_after) / 2 # Frequency at which signal begins
lon17_error = (lon17_freq_after - lon17_freq_before) / 2 # Error bound as described above the def for find_first_signal
lon17_freq = round(lon17_freq, 7) # Rounding frequency to 7 decimal places (precision of measurements)
lon17_error = round(lon17_error, 7) # Rounding error similarly

# Plotting spectrum for longitude 17 data
plt.figure()
plt.plot(lon17[:,0], lon17[:,1], label="Spectrum") # Plot spectrtum

 # Plot freqcy at which signal exceeds 5 K
plt.axvline(x = lon17_freq, linestyle="--", color="orange", label=str(lon17_freq) + " MHz")

plt.xlabel("Frequency (MHz)")
plt.ylabel("Brightness Temperature (K)")
plt.title("Spectrum for Galactic Longitude of 17 degrees")
plt.legend()
plt.gcf().savefig(fname="./images/lon17.png", dpi=300)
plt.show()

'''
Iterating through all datasets and outputting all their neutral hydrogen emission line frequencies, plus plotting.
This is commented out after all data is read in and can be uncommented easily.

longitudes = [17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65] # all longitudes in data
for lon in longitudes:
    cur_lon = load_lon(lon) # Loading longitude data from file
    freq_before, freq_after = find_first_signal(cur_lon) # Finding the first signal frequencies as described above
    freq = (freq_before + freq_after) / 2 # Frequency at which signal begins
    error = (freq_after - freq_before) / 2 # Error bound
    freq = round(freq, 7) # Rounding frequency
    error = round(error, 7) # Rounding error

    # Plotting:
    plt.figure()
    plt.plot(cur_lon[:,0], cur_lon[:,1], label="Spectrum")
    plt.axvline(x = freq, linestyle = "--", color="orange", label=str(freq) + " MHz")
    plt.xlabel("Frequency (MHz)")
    plt.ylabel("Brightness Temperature (K)")
    plt.title("Spectrum for Galactic Longitude of " + str(lon) + " degrees")
    plt.legend()
    plt.gcf().savefig(fname="./images/lon" + str(lon) + ".png", dpi=300)
    plt.show()

    print(f"", lon, "\t", freq, "\t", error, "\t", freq_before, "\t", freq_after)
'''

'''
Plotting the velocity curve as calculated from the observed frequencies and angles;
uncertainties are also plotted.
'''
# Getting the data as calculated in our spreadsheet as well as uncertainties
v_curve_values = np.genfromtxt("./v_curve.fred")
uncertainties = np.genfromtxt("./uncertainties.fred")
velocities = v_curve_values[:,0]
radii = v_curve_values[:,1]
sigma_v = uncertainties[:,0]
sigma_r = uncertainties[:,1]
# Plotting the data
plt.figure()
plt.plot(radii, velocities)
plt.errorbar(x=radii, y=velocities, xerr=sigma_r, yerr=sigma_v, fmt="o")
plt.xlabel("Distance from center (kpc)")
plt.ylabel("Orbital velocity (km/s)")
plt.title("Velocity curve of the Milky Way")
plt.savefig("./images/v_curve.png", dpi=300)
plt.show()

# Creating a function to fit to; function is of the form ax^b
def power_fit(x, a, b):
    return a * (x ** b)

# Function to fit to of the form ae^bx
def exp_fit(x, a, b):
    return a * np.exp(b * x)

# Function to fit to of the form alog(bx)
def log_fit(x, a, b):
    return a * np.log(b * x)

# Function to fit to of the form ax + b
def line_fit(x, a, b):
    return a * x + b

# Testing different fitted curves for data
popt_pow, pcov_pow = curve_fit(power_fit, radii, velocities) # Power curve fit
popt_exp, pcov_exp = curve_fit(exp_fit, radii, velocities) # Exponential curve fit
popt_log, pcov_log = curve_fit(log_fit, radii, velocities) # Logarithmic curve fit
popt_lin, pcov_lin = curve_fit(line_fit, radii, velocities) # Linear curve fit

# Function to find the R^2 value of a fitted curve
def R_squared(velocities, radii, function, *popt):
    residuals = velocities - function(radii, *popt)
    sum_squares_res = np.sum(residuals ** 2)
    sum_squares_tot = np.sum((velocities - np.mean(velocities)) ** 2)
    return 1 - (sum_squares_res / sum_squares_tot)

# Finding R^2 values for each fit
R_sq_pow = R_squared(velocities, radii, power_fit, *popt_pow) # Power curve fit R^2
R_sq_exp = R_squared(velocities, radii, exp_fit, *popt_exp) # Exp curve fit R^2
R_sq_log = R_squared(velocities, radii, log_fit, *popt_log) # Log curve fit R^2
R_sq_lin = R_squared(velocities, radii, line_fit, *popt_lin) # Line curve fit R^2

# Plotting best fit curve onto the observed curve
plt.figure()
plt.plot(radii, velocities)
plt.errorbar(x = radii, y = velocities, xerr = sigma_r, yerr = sigma_v, fmt = "o", label="Observed")
# Plotting best fit curve for a power function
plt.plot(radii, power_fit(radii, *popt_pow), label="v = " + str(popt_pow[0])[0:5] + "r^" + str(popt_pow[1])[0:5] + ", R^2 = " + str(R_sq_pow)[0:5])
# Plotting best fit curve for an exponential function
plt.plot(radii, exp_fit(radii, *popt_exp), label="v = " + str(popt_exp[0])[0:5] + "e^" + str(popt_exp[1])[0:5] + "r, R^2 = " + str(R_sq_exp)[0:5])
# Plotting best fit curve for a logarithmic function
plt.plot(radii, log_fit(radii, *popt_log), label="v = " + str(popt_log[0])[0:5] + "log(" + str(popt_exp[1])[0:5] + "r), R^2 = " + str(R_sq_log)[0:5])
# Plotting best fit curve for a linear function
plt.plot(radii, line_fit(radii, *popt_lin), label="v = " + str(popt_exp[0])[0:5] + "r + " + str(popt_exp[1])[0:5] + ", R^2 = " + str(R_sq_lin)[0:5])
plt.xlabel("r = Distance from center (kpc)")
plt.ylabel("v = Orbital velocity (km/s)")
plt.title("Velocity curve of the Milky Way with multiple best fit curves")
plt.legend(loc="lower right")
plt.savefig("./images/v_curve_fit_multiple.png", dpi=300)
plt.show()

# Plotting singular best fit curve (log)
plt.figure()
plt.plot(radii, velocities)
plt.errorbar(x = radii, y = velocities, xerr = sigma_r, yerr = sigma_v, fmt = "o", label="Observed")
plt.plot(radii, log_fit(radii, *popt_log), label="v = " + str(popt_log[0])[0:5] + "log(" + str(popt_exp[1])[0:5] + "r), R^2 = " + str(R_sq_log)[0:5])
plt.xlabel("r = Distance from center (kpc)")
plt.ylabel("v = Orbital velocity (km/s)")
plt.title("Velocity curve of the Milky Way with logarithmic fit curve")
plt.legend(loc="lower right")
plt.savefig("./images/v_curve_fit.png", dpi=300)
plt.show()