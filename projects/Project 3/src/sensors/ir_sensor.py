from basehat import IRSensor


class InfraredSensor:
    """Infrared sensor of GEARS."""

    def __init__(self) -> None:
        """Create infrared sensor."""

        self.sensor = IRSensor(26)

    @property
    def left(self) -> float:
        """Left infrared sensor value."""

        return self.sensor.value1

    @property
    def right(self) -> float:
        """Left infrared sensor value."""

        return self.sensor.value2
