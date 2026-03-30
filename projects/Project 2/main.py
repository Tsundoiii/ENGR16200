import math
from tower import Tower
from particle import Particle

base_tower = Tower(1, 3 * 0.21, 750)
tower = base_tower

pm25 = Particle(1e-10, 1.6e-16, 2.5e-6, 1.628e-8, 5e-9)
pm10 = Particle(1e-10, 1.6e-16, 10e-6, 3.3e-8, 15e-9)

pm25.towers(tower)
print()
pm10.towers(tower)
