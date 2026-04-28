from basehat import UltrasonicSensor


class DistanceSensor:
    """Distance sensor of GEARS."""

    def __init__(self) -> None:
        """Create distance sensor."""

        self.front_sensor = UltrasonicSensor(5)
        self.left_sensor = UltrasonicSensor(22)
        self.right_sensor = UltrasonicSensor(26)

        self.distance_threshold = 40

    @property
    def front_distance(self) -> float | None:
        """Distance of nearest object in front of GEARS (in cm), or None if no objects detected."""

        return self.front_sensor.getDist

    @property
    def left_distance(self) -> float | None:
        """Distance of nearest object to the left of GEARS (in cm), or None if no objects detected."""

        return self.left_sensor.getDist

    @property
    def right_distance(self) -> float | None:
        """Distance of nearest object to the right of GEARS (in cm), or None if no objects detected."""

        return self.right_sensor.getDist

    @property
    def front_clear(self) -> bool:
        distance = self.front_distance

        return distance is None or distance > self.distance_threshold

    @property
    def left_clear(self) -> bool:
        distance = self.left_distance

        return distance is None or distance > self.distance_threshold

    @property
    def right_clear(self) -> bool:
        distance = self.right_distance

        return distance is None or distance > self.distance_threshold

    @property
    def all_clear(self) -> bool:
        return self.front_clear and self.left_clear and self.right_clear

    def log(self) -> None:
        """Log distance (in cm) of object in front of GEARS."""

        print(
            f"[Distance Sensor] Front: {self.front_distance} cm | Left: {self.left_distance} cm | Right: {self.right_distance} cm"
        )
