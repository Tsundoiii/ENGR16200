#drag_force
#buoyant_force
#grav_force
#e_field_force

import math

def drag_force(velocity: float, fluid_density: float, drag_coefficient: float, diameter: float) -> float:
    return 0.5 * fluid_density * drag_coefficient * (math.pi/4) * diameter**2 * velocity * abs(velocity)

def buoyant_force(fluid_density: float, diameter: float) -> float:
    return (math.pi/6) * fluid_density * diameter**3

def grav_force(fluid_density: float, diameter: float) -> float:
    return (math.pi/6) * fluid_density * diameter**3

def e_field_force(cloud_density: float, distance: float, height: float) -> float:
    return (cloud_density/(2*8.854187817e-12)) * ((2 * distance) - height)