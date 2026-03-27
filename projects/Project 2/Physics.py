

import math

def drag_force(viscosity: float, diameter: float, velocity: float) -> float:
    return 3 * math.pi * viscosity * diameter * velocity

def buoyant_force(fluid_density: float, diameter: float) -> float:
    return fluid_density * 9.81 * particle_volume

def grav_force(particle_density: float, diameter: float) -> float:
    return particle_density * 9.81 * particle_volume

def e_field_force(charge: float, electric_field: float) -> float:
    return charge * electric_field

velocity = 0 #m/s
fluid_density = 1.225 #kg/m^3
drag_coefficient = 0.47
diameter = 5e-6 #m
particle_volume = (math.pi/6) * diameter**3 #m^3
particle_density = 1200 #kg/m^3
particle_mass = particle_density * particle_volume
timestep = 1e-4 #s
time = 0 #s
charge = 1.6e-16 #C
electric_field = 1e5 #V/m
viscosity = 1.81e-5 #Pa.s

choice = input("Do you want to perform cottor's method, Calculate using regular variables, or calculate using your own changes to components? (cottor/regular/own): ")

if choice == "cottor":
    print ("cottor's method is not implemented yet") 
elif choice == "regular":

    counter = 0
    max_count = 1000000
    distance = 5
    while distance > 0 and counter < max_count:
        net_force = e_field_force(charge, electric_field) \
            + grav_force(particle_density, particle_volume) \
            - buoyant_force(fluid_density, particle_volume) \
            - drag_force(viscosity, diameter, velocity)
        counter += 1
        acceleration = net_force / particle_mass
        velocity += acceleration * timestep
        distance -= velocity * timestep
        time += timestep
    print(f"Time: {time:.5f} s, Distance: {distance:.5f} m, Velocity: {velocity:.5f} m/s")    
        


else:
    print ("own method is not implemented yet")

