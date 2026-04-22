from basehat import UltrasonicSensor


class DistanceSensor:
    """Distance sensor of GEARS."""

    def __init__(self) -> None:
        """Create distance sensor."""

        self.front_sensor = UltrasonicSensor(18)
        # self.left_sensor = UltrasonicSensor(0)
        self.right_sensor = UltrasonicSensor(26)

        self.distance_threshold = 20

    @property
    def front_distance(self) -> float | None:
        """Distance of nearest object in front of GEARS (in cm), or None if no objects detected."""
        
        print("Front dist:" + str(self.front_sensor.getDist))
        return self.front_sensor.getDist
    
    # @property
    # def left_distance(self) -> float | None:
    #     """Distance of nearest object to the left of GEARS (in cm), or None if no objects detected."""

    #     return self.left_sensor.getDist
    
    @property
    def right_distance(self) -> float | None:
        """Distance of nearest object to the right of GEARS (in cm), or None if no objects detected."""
        print("Right dist:" + str(self.right_sensor.getDist))
        return self.right_sensor.getDist
    
    @property
    def front_clear(self) -> bool:
        distance = self.front_distance
        return distance is None or distance > self.distance_threshold
    
    # @property
    # def left_clear(self) -> bool:
    #     return self.left_distance is not None and self.left_distance > self.distance_threshold
    
    @property
    def right_clear(self) -> bool:
        distance = self.right_distance
        return distance is None or distance > self.distance_threshold
    
    @property
    def all_clear(self) -> bool:
        return self.front_clear and self.right_clear

    def log(self) -> None:
        """Log distance (in cm) of object in front of GEARS."""

        print(f"[Distance Sensor] Distance: {self.front_distance} cm")
