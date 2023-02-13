import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# dataset size, period, amplitude, and number of days to be used later
size = 75
period = 25
amplitude = 80
days = 50

'''
Function to generate synthetic exoplanet signal;
accepts an array of time values in days, period in days,
and maximum radial velocity in meters per second, and
returns an array of radial velocity values corresponding
to a sinusoidal curve with the given parameters as period
and amplitude.
'''
def exoplanet_signal(time_inputs, period, amplitude):
    return np.sin((time_inputs * 2 * np.pi) / period) * amplitude

# plotting exoplanet signal without noise
plt.figure()
input = np.linspace(0, days, size)
signal_no_noise = exoplanet_signal(input, period, amplitude) # exoplanet with period of 10 days, max radial vel of 80 m/s
plt.plot(input, signal_no_noise)
plt.title("Exoplanet velocity over 50 days without noise")
plt.xlabel("Days")
plt.ylabel("Radial velocity (m/s)")
plt.show()

# generating random noise in signal
noise = np.random.uniform(-0.12 * amplitude, 0.12 * amplitude, size)
signal_with_noise = signal_no_noise + noise

# plotting exoplanet signal with noise
plt.figure()
plt.plot(input, signal_with_noise)
plt.title("Exoplanet velocity over 50 days with noise")
plt.xlabel("Days")
plt.ylabel("Radial velocity (m/s)")
plt.show()

# calculating standard deviation of noise and showing on plot
std_dev = np.std(noise)
plt.figure()
plt.title("Exoplanet velocity over 50 days with noise and error bars")
plt.xlabel("Days")
plt.ylabel("Radial velocity (m/s)")
plt.errorbar(input, signal_with_noise, yerr = std_dev, ls = "none", marker = ".", ecolor = "blue", elinewidth = 1)
plt.show()

# fitting noisy data to a curve using scipy
p0 = [25.55, 76.00]
params, cov = curve_fit(exoplanet_signal, input, signal_with_noise, p0)
y_fit = exoplanet_signal(input, params[0], params[1])
one_sigma = np.sqrt(np.diag(cov))
print("Fit period: ", params[0], " Amplitude: ", params[1])
print("One sigma uncertainty: ", one_sigma)

# plotting noisy data with fit curve
plt.figure()
plt.title("Exoplanet velocity over 50 days")
plt.xlabel("Days")
plt.ylabel("Radial velocity (m/s)")
plt.plot(input, y_fit, "--", color = "gray")
plt.errorbar(input, signal_with_noise, yerr = std_dev, ls = "none", marker = ".", ecolor = "blue", elinewidth = 1)
plt.show()