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
threshold = 5
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
plt.axvline(x = lon17_freq, linestyle="--", color="orange", label=str(round(lon17_freq, 3)) + " MHz")

plt.xlabel("Frequency (MHz)")
plt.ylabel("Brightness Temperature (K)")
plt.title("Spectrum for Galactic Longitude of 17 degrees, threshold of 5 K")
plt.legend()
plt.gcf().savefig(fname="./images/lon17_5K.png", dpi=300)
plt.show()

'''
Iterating through all datasets and outputting all their neutral hydrogen emission line frequencies, plus plotting.
This is commented out after all data is read in and can be uncommented easily.
'''
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
    plt.axvline(x = freq, linestyle = "--", color="orange", label=str(round(freq, 3)) + " MHz")
    plt.xlabel("Frequency (MHz)")
    plt.ylabel("Brightness Temperature (K)")
    plt.title("Spectrum for Galactic Longitude of " + str(lon) + " degrees, threshold of 5 K")
    plt.legend()
    plt.gcf().savefig(fname="./images/lon_5K" + str(lon) + ".png", dpi=300)
    plt.show()

    print(f"", lon, "\t", freq, "\t", error, "\t", freq_before, "\t", freq_after)

'''
Plotting the rotation curve as calculated from the observed frequencies and angles;
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
plt.errorbar(x=radii, y=velocities, xerr=sigma_r, yerr=sigma_v, fmt="o")
plt.xlabel("Distance from center (kpc)")
plt.ylabel("Orbital velocity (km/s)")
plt.title("Rotation curve of the Milky Way with a threshold of 5 K")
plt.savefig("./images/v_curve_5K.png", dpi=300)
plt.show()