import numpy as np
import matplotlib.pyplot as plt

G = 4.3e-6 # Gravitational constant in kpc * M_sun^-1 * (km/s)^2

Mr = 1.5e12 # Mass of the Milky Way
r15 = np.linspace(1, 15, 500) # array of kiloparsec radii for plotting

def v_orb(Mr, r):
    return np.sqrt((G * Mr) / r)

def mass_propto_r(r):
    return (Mr / 15) * r

def mass_propto_cube(r):
    return (Mr / (15** 3)) * (r ** 3)

def mass_central_sphere(r):
    result = np.copy(r)
    for i in range(0, np.size(r)):
        if (r[i] < 2):
            result.put(indices=i, values= (((0.05 * Mr) / (2 ** 3)) * (r[i] ** 3)))
        else:
            result.put(indices=i, values=(0.05 * Mr))
    return result

v_point = v_orb(Mr, r15) # Array of velocities corresponding to radii for all mass at center as a point source
v_lin = v_orb(mass_propto_r(r15), r15) # Velocities corresponding to radii for mass increasing linearly
v_cube = v_orb(mass_propto_cube(r15), r15) # Velocities ... for mass increasing cubicly

r = np.linspace(0.5, 8, 500)
v_central_sphere = v_orb(mass_central_sphere(r), r) # Velocities ... mass is contained in a central sphere to 2 pc, 
                                                    # after which it is negligible


# Plotting the orbital velocity curves
plt.figure()
plt.plot(r15, v_point, label="Point source") # point source of mass at center
plt.plot(r15, v_lin, label="Linear") # mass increases linearly with radius
plt.plot(r15, v_cube, label="Cubic") # mass increases with the cube of the radius

plt.xlabel("Distance from center (kpc)")
plt.ylabel("Speed (km/s)")
plt.title("Orbital rotation curves")
plt.legend()
plt.savefig("./images/hypothetical_v_curves.png", dpi=300)
plt.show()

# Plotting the velocity curve for the theoretical galaxy where most mass is in the central 2 kpc
plt.figure()
plt.plot(r, v_central_sphere, label="Central sphere") # mass increases with the central sphere
plt.xlabel("Distance from center (kpc)")
plt.ylabel("Speed (km/s)")
plt.title("Theoretical Milky Way rotation curve")
plt.savefig("./images/hypothetical_milky_way_curve.png", dpi=300)
plt.show()