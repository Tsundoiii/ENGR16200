import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, 1)

mag_dist = np.genfromtxt("data/magDist.csv", delimiter=",", dtype=None, names=True, usecols=("Distance", "Magnitude"))

distances, magnitudes = zip(*mag_dist)
ax1.scatter(distances, magnitudes)
ax1.set_xlabel("Distance (cm)")
ax1.set_ylabel("Magnetic Field Magnitude (mT)")

mag_angle = np.genfromtxt("data/magAngle.csv", delimiter=",", dtype=None, names=True, usecols=("Angle", "Magnitude"))

angles, magnitudes = zip(*mag_angle)
angles = [angle.split()[0] for angle in angles]
ax2.scatter(angles, magnitudes)
ax2.set_xlabel("Angle (deg)")
ax2.set_ylabel("Magnetic Field Magnitude (mT)")

plt.show()