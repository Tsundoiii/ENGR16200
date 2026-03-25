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

velocity = 0
fluid_density = 1.225
drag_coefficient = 0.47
diameter = 0.1

input("Do you want to perform cottor's method, Calculate using regular variables, or calculate using your own changes to components? (cottor/regular/own): ")

if input == "cottor":
    return "cottor's method is not implemented yet" 
elif input == "regular":
    counter = 0
    max_count = 1000
    d = 5
    while d > 0
        y_value = buoyant_force(fluid_density, diameter) - grav_force(fluid_density, diameter)
        x_value = e_field_force(1e-6, 1, 1) - drag_force(velocity, fluid_density, drag_coefficient, diameter)
        d = d-x_value


else:
     

