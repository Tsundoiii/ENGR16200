from math import isclose
from basehat import IRSensor


class InfraredSensor:
    """Infrared sensor of GEARS."""

    def __init__(self) -> None:
        """Create infrared sensor."""

        self.sensor = IRSensor(0, 1)
        self.threshold = 30
        self.absolute_tolerance = 0.5

    @property
    def left(self) -> float:
        """Left infrared sensor value."""

        return self.sensor.value1

    @property
    def right(self) -> float:
        """Left infrared sensor value."""

        return self.sensor.value2

    @property
    def value(self) -> float:
        """Average value of left and right IR sensors."""

        return (self.left + self.right) / 2
    
    @property
    def source_present(self) -> bool:
        return self.value > self.threshold
    
    @property
    def source_direction(self) -> tuple[int, int]:
        if isclose(self.left, self.right, rel_tol=self.absolute_tolerance):
            return (0, 1)
        elif self.right > self.left:
            return (1, 0)
        else:
            return (-1, 0)

    def log(self) -> None:
        """Log infrared sensor average value."""

        print(f"[Infrared Sensor] | Value: {self.value} | Left: {self.left} | Right: {self.right} | Present: {self.source_present}")
