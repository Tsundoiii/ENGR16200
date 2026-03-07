from buildhat import Motor


class Drivetrain:
    """Drivetrain of GEARS."""

    def __init__(self) -> None:
        """Create drivetrain of GEARS."""

        self.left_motor = Motor("C")
        self.right_motor = Motor("D")

        self.gear_ratio = 0  # TODO
        self.unit_distance = 40

    def drive_differential(self, left_speed: float, right_speed: float):
        """
        Drive each drivetrain motor with different speeds. Positive speed indicates clockwise rotation of the motor.

        :param left_speed: speed of left motor
        :param right_speed: speed of right motor
        """

        pass

    def drive_with_speed(self, speed: float) -> None:
        """
        Drive drivetrain with a speed. Positive speed indicates forward motion relative to robot.

        :param speed: speed to drive at
        """

        pass

    def drive_distance(self, distance: float) -> None:
        """
        Drive drivetrain for a distance. Positive distance indicates forward motion relative to robot.

        :param distance: distance to drive to (in cm)
        """

        pass

    def drive_units(self, units: float) -> None:
        """
        Drive drivetrain for a number of unit distances. Positive distance indicates forward motion relative to robot.

        :param units: number of units to drive to
        """

        pass

    def stop(self) -> None:
        """Stop the drivetrain."""

        pass
