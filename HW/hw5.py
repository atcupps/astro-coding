import numpy as np
import matplotlib.pyplot as plt

# Gravitational constant in solar masses, km/s, and kpc
G = 4.3e-6
# Orbital velocity from mass and radius
def v_orbital(mass, radius):
    return np.sqrt((mass * G) / radius)

# Radii ranging from 0.1 to 30 kpc
radius = np.linspace(0.1, 30, 500)
# Masses corresponding to each radius; mass propto r^1.2
# The mass is scaled so that the largest mass yields a velocity of 200 km/s.
mass = radius ** 1.2
print(((200 ** 2) * radius.max() / G) / mass.max())
mass *= ((200 ** 2) * radius.max() / G) / mass.max()
# Orbital velocity at each radius
velocity = v_orbital(mass, radius)

# Plotting mass as a function of radius
plt.figure()
plt.plot(radius, mass)
plt.xlabel("Distance from center (kpc)")
plt.ylabel("Enclosed mass (solar masses)")
plt.title("Enclosed mass profile for M prop. to r^1.2")
plt.savefig("./images/hw5_m_profile.png", dpi=300)
plt.show()

# Plotting velocity curve
plt.figure()
plt.plot(radius, velocity)
plt.xlabel("Distance from center (kpc)")
plt.ylabel("Orbital velocity (km/s)")
plt.title("Orbital velocity curve for M prop. to r^1.2")
plt.savefig("./images/hw5_v_curve.png", dpi=300)
plt.show()