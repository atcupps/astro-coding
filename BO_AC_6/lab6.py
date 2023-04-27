import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

# Making plots wide to take up entire screen
plt.rcParams['figure.figsize'] = [16, 4]

f = fits.open("./Galaxies/NGC_1832.fits")
data = f[0].data

# from 3650 to 7100 by 2
start = 3650
stop = 7101
step = 2
wavelengths = np.arange(start, stop, step)

# Wavelength for K, H, and H-alpha at rest
K_rest = 3934.777
H_rest = 3969.588
Ha_rest = 6564.61

print("Galaxy\tCa K\tCa H\tH-alpha")

# Function that takes in data and estimates for K, H, and H-alpha, and plots it
# Also prints all data
def plotSpectrum(data, K, H, Ha, name):
    plt.figure()
    plt.axvline(K, label="Ca K: " + str(K), linestyle="--", color="orange", linewidth=1)
    plt.axvline(H, label="Ca H: " + str(H), linestyle="--", color="red", linewidth=1)
    plt.axvline(Ha, label="H-alpha: " + str(Ha), linestyle="--", color="gold", linewidth=1)
    plt.plot(wavelengths, data, label="Spectrum", linewidth=1)
    
    # Labels and stuff
    plt.legend()
    plt.xlabel("Wavelength (Angstroms)")
    plt.ylabel("Intensity (normalized)")
    plt.title("Spectrum of NGC " + str(name))

    plt.savefig("./Images/Spectra/Spectra_NGC_" + str(name) + ".png", dpi=300)

    plt.show()

    # Printing tab-delimited data
    print("NGC " + str(name) + "\t" + str(K) + "\t" + str(H) + "\t" + str(Ha))

# Plotting for NGC 1832
K_line = 3960
H_line = 3996
Ha_line = 6608
plotSpectrum(data, K_line, H_line, Ha_line, 1832)

# NGC 2276
f = fits.open("./Galaxies/NGC_2276.fits")
data = f[0].data
K_line = 3966
H_line = 3996
Ha_line = 6616
plotSpectrum(data, K_line, H_line, Ha_line, 2276)

# NGC 2798
f = fits.open("./Galaxies/NGC_2798.fits")
data = f[0].data
K_line = 3954
H_line = 3992
Ha_line = 6602
plotSpectrum(data, K_line, H_line, Ha_line, 2798)

# NGC 2903
f = fits.open("./Galaxies/NGC_2903.fits")
data = f[0].data
K_line = 3938
H_line = 3972
Ha_line = 6574
plotSpectrum(data, K_line, H_line, Ha_line, 2903)

# NGC 3034
f = fits.open("./Galaxies/NGC_3034.fits")
data = f[0].data
K_line = 3936
H_line = 3972
Ha_line = 6564
plotSpectrum(data, K_line, H_line, Ha_line, 3034)

# NGC 3147
f = fits.open("./Galaxies/NGC_3147.fits")
data = f[0].data
K_line = 3968
H_line = 4002
Ha_line = 6622
plotSpectrum(data, K_line, H_line, Ha_line, 3147)

# NGC 3368
f = fits.open("./Galaxies/NGC_3368.fits")
data = f[0].data
K_line = 3946
H_line = 3980
Ha_line = 6584 # 6606 ??
plotSpectrum(data, K_line, H_line, Ha_line, 3368)

# NGC 3627
f = fits.open("./Galaxies/NGC_3627.fits")
data = f[0].data
K_line = 3942
H_line = 3978
Ha_line = 6578
plotSpectrum(data, K_line, H_line, Ha_line, 3627)

# NGC 4750
f = fits.open("./Galaxies/NGC_4750.fits")
data = f[0].data
K_line = 3954
H_line = 3992
Ha_line = 6592
plotSpectrum(data, K_line, H_line, Ha_line, 4750)

# NGC 4775
f = fits.open("./Galaxies/NGC_4775.fits")
data = f[0].data
K_line = 3958
H_line = 3990
Ha_line = 6596
plotSpectrum(data, K_line, H_line, Ha_line, 4775)

# NGC 5195
f = fits.open("./Galaxies/NGC_5195.fits")
data = f[0].data
K_line = 3942
H_line = 3976
Ha_line = 6594
plotSpectrum(data, K_line, H_line, Ha_line, 5195)

# NGC 5248
f = fits.open("./Galaxies/NGC_5248.fits")
data = f[0].data
K_line = 3946
H_line = 3982
Ha_line = 6586
plotSpectrum(data, K_line, H_line, Ha_line, 5248)

# NGC 6181
f = fits.open("./Galaxies/NGC_6181.fits")
data = f[0].data
K_line = 3966
H_line = 4000
Ha_line = 6610
plotSpectrum(data, K_line, H_line, Ha_line, 6181)

# NGC 6643
f = fits.open("./Galaxies/NGC_6643.fits")
data = f[0].data
K_line = 3952
H_line = 3986
Ha_line = 6594
plotSpectrum(data, K_line, H_line, Ha_line, 6643)