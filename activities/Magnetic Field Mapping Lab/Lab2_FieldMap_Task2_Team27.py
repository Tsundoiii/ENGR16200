import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2,1 )

mag_data = np.genfromtxt("data/FieldMagData.csv", delimiter=",", dtype=None, usecols=(1, 2, 3, 4))[1:5].transpose()

ax1.imshow(mag_data, cmap="hot", interpolation="nearest", extent=[0, 4, 4, 0])
ax1.invert_yaxis()

vec_x = np.genfromtxt("data/FieldVecData.csv", delimiter=",", dtype=None, usecols=range(1, 13, 3))[1:].transpose()
vec_y = np.genfromtxt("data/FieldVecData.csv", delimiter=",", dtype=None, usecols=range(2, 14, 3))[1:].transpose()
axes = np.arange(4)
x, y = np.meshgrid(axes, axes)
ax2.quiver(x, y, vec_x, vec_y)

plt.show()