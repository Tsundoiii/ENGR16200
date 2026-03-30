from dataclasses import dataclass
from math import pi


@dataclass
class Particle:
    mass: float
    charge: float  # C
    diameter: float  # m
    particle_density: float  # particle / m^3
    target_density: float

    fluid_density = 1.225  # kg/m^3
    viscosity = 1.81e-5  # Pa.s
    g = 9.81
    distance = 1
    velocity = 0

    @property
    def concentration(self):
        return self.particle_density / self.mass

    @property
    def target_concentration(self):
        return self.target_density / self.mass

    @property
    def particle_volume(self):
        return pi / 6 * self.diameter**3  # m^3

    @property
    def drag_force(self) -> float:
        return 3 * pi * self.viscosity * self.diameter * self.velocity

    @property
    def buoyant_force(self) -> float:
        return self.fluid_density * self.g * self.particle_volume

    @property
    def grav_force(self) -> float:
        return self.mass * self.g

    def e_field_force(self, electric_field: float) -> float:
        return self.charge * electric_field

    def flow(self, tower):
        timestep = 1e-4  # s
        time = 0  # s

        counter = 0
        max_count = 1000000

        while self.distance > 0 and counter < max_count:
            net_force = (
                -self.e_field_force(tower.charge_density)
                - self.grav_force
                + self.buoyant_force
                + self.drag_force
            )

            self.acceleration = net_force / self.mass
            self.velocity += self.acceleration * timestep
            self.distance += self.velocity * timestep

            counter += 1
            time += timestep

        flow = self.concentration * tower.area / time

        if counter == max_count:
            print("FAILED TO FINISH")

        print(f"Time: {time:.5f} s")
        print(f"Distance: {self.distance:.5f} m")
        print(f"Velocity: {self.velocity:.5f} m/s")
        print(f"Flow: {flow:.5f} particle / sec")
        # print(f"Power consumption: {tower.power_consumption} J / day")

        return flow

    def towers(self, tower):
        towers = (
            500e9 * self.target_concentration / self.flow(tower) / 60 / 60 / 24 / 365
        )

        print(f"Towers needed: {towers}")
