from basehat import UltrasonicSensor


class DistanceSensor:
    """Distance sensor of GEARS."""

    def __init__(self) -> None:
        """Create distance sensor."""

        self.sensor = UltrasonicSensor(18)

    @property
    def distance(self) -> float | None:
        """Distance of nearest object in front of sensor (in cm), or None if no objects detected."""

        return self.sensor.getDist

    def log(self) -> None:
        """Log distance (in cm) of object in front of GEARS."""

        print(f"[Distance Sensor] Distance: {self.distance} cm")
