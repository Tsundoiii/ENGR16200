from dataclasses import dataclass


@dataclass
class Tower:
    charge_density: float
    area: float
    power: float

    @property
    def electric_field(self):
        return self.charge_density / 2 / 8.854e-12

    @property
    def power_consumption(self):
        return self.power * 60 * 60 * 24
