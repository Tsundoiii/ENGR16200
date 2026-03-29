

import math

def drag_force(viscosity: float, diameter: float, velocity: float) -> float:
    return 3 * math.pi * viscosity * diameter * velocity

def buoyant_force(fluid_density: float, particle_volume: float) -> float:
    return fluid_density * 9.81 * particle_volume

def grav_force(particle_density: float, particle_volume: float) -> float:
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
timestep = 1e-5 #s
time = 0 #s
charge = 1.6e-16 #C
electric_field = 1e5 #V/m
viscosity = 1.81e-5 #Pa.s
fan_energy = 1500 #W
Tower_height = 7 #m
tower_radius = 1.5 #m
tower_volume = math.pi * tower_radius**2 * Tower_height #m^3
tower_panel_surface_area = 2 * math.pi * tower_radius * Tower_height #m^2
power_density = 2.5 #W/m^2
electric_field_energy = power_density * tower_panel_surface_area #W

choice = input("Do you want to perform cotter's method, Calculate using regular variables, or calculate using your own changes to components? (cotter/regular/own): ")

if choice == "cotter":

    def run_simulation(electric_field: float, diameter: float, charge: float) -> float:
        counter = 0
        max_count = 3000000
        distance = 0.1 #m
        velocity = 0 #m/s
        time = 0 #s

        new_particle_volume = (math.pi/6) * diameter**3 #m^3
        new_particle_mass = particle_density * new_particle_volume


        while distance > 0 and counter < max_count:
            net_force = e_field_force(charge, electric_field) \
                + grav_force(particle_density, new_particle_volume) \
                - buoyant_force(fluid_density, new_particle_volume) \
                - drag_force(viscosity, diameter, velocity)
            counter += 1
            acceleration = net_force / new_particle_mass
            velocity += acceleration * timestep
            distance -= velocity * timestep
            time += timestep

        if time <= 3e10:
            cleaning_rate = (tower_volume / time)*3600 #m^3/h
        else:
            cleaning_rate = 0

        kilowatts_energy = (fan_energy / 1000) + (electric_field_energy / 1000)
        return cleaning_rate, kilowatts_energy

    variables = ["Electric Field", "Diameter", "Charge"]
    lows = [0.8e5, 2.0e-6, 1.2e-16]
    highs = [1.2e5, 8.0e-6, 2.0e-16]
    m = len(variables)

    y = [0.0] * (2 * m + 2)

    y[0] = run_simulation(lows[0], lows[1], lows[2])[0]

    for i in range(m):
        v = lows[:]
        v[i] = highs[i]
        y[i + 1] = run_simulation(v[0], v[1], v[2])[0]

    y[m + 1] = run_simulation(highs[0], highs[1], highs[2])[0]

    for i in range(m):
        v = highs[:]
        v[i] = lows[i]
        y[m + 2 + i] = run_simulation(v[0], v[1], v[2])[0]

    results = []
    total_impact = 0
    for i in range(m):
        low_i = y[i + 1] - y[0]
        high_i = y[m + 1] - y[m + 2 + i]
        effect_magnitude = abs(low_i) + abs(high_i)
        results.append(effect_magnitude)
        total_impact += effect_magnitude

    print(f"\n{'Variable':<20} | {'Impact %':<15}")
    print("-" * 38)
    for i in range(m):
        percent = (results[i] / total_impact) if total_impact > 0 else 0
        print(f"{variables[i]:<15} | {percent:<8.2f}Normalized Effect Measure")

elif choice == "regular":

    counter = 0
    max_count = 3000000
    distance = 0.1 #m

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

    if time <= 3e10:
        cleaning_rate = (tower_volume / time)*3600 #m^3/h
    else:
        cleaning_rate = 0

    kilowatts_energy = (fan_energy / 1000) + (electric_field_energy / 1000)
    
    print(f"Time to capture particle: {time:.5f} s, Final velocity: {velocity:.5f} m/s, Volume cleaned per hour: {cleaning_rate:.2f} m^3/h, Energy used: {kilowatts_energy:.2f} kW") 
    

elif choice == "own":

    Tower_height = float(input("Enter tower height in meters: "))
    tower_radius = float(input("Enter tower radius in meters: "))  
    tower_volume = math.pi * tower_radius**2 * Tower_height #m^3
    tower_panel_surface_area = 2 * math.pi * tower_radius * Tower_height #m^2
    power_density = float(input("Enter power density in W/m^2: "))
    electric_field_energy = power_density * tower_panel_surface_area #W
    number_of_towers = int(input("Enter number of towers: "))

    counter = 0
    max_count = 3000000
    distance = 0.1 #m

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

    if time <= 3e10:
        cleaning_rate = (tower_volume / time)*3600*number_of_towers #m^3/h
    else:
        cleaning_rate = 0

    kilowatts_energy = ((fan_energy / 1000) + (electric_field_energy / 1000)) * number_of_towers
    
    print(f"Time to capture particle: {time:.5f} s, Final velocity: {velocity:.5f} m/s, Volume cleaned per hour: {cleaning_rate:.2f} m^3/h, Energy used: {kilowatts_energy:.2f} kW") 
    

else:
    print("Invalid choice")