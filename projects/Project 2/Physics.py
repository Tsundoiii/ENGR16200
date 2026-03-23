#drag_force
#buoyant_force
#grav_force
#e_field_force

import math

def drag_force(velocity: float, fluid_density: float, drag_coefficient: float, diameter: float) -> float:
    area = 3.14159 * (diameter / 2) ** 2
    return 0.5 * fluid_density * drag_coefficient * area * velocity * abs(velocity)