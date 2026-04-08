from basehat import IRSensor


class InfraredSensor:
    """Infrared sensor of GEARS."""

    def __init__(self) -> None:
        """Create infrared sensor."""

        self.sensor = IRSensor(0, 1)

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

    def log(self) -> None:
        """Log infrared sensor average value."""

        print(f"[Infrared Sensor] {self.value}")
