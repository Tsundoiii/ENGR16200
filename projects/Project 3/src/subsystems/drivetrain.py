from math import pi
from time import sleep
from buildhat import Motor
from basehat import IMUSensor
import numpy as np


class Drivetrain:
    """Drivetrain of GEARS."""

    def __init__(self) -> None:
        """Create drivetrain of GEARS."""

        self.imu = IMUSensor()

        self.left_motor = Motor("D")
        self.right_motor = Motor("C")

        self.wheel_radius = 3.4
        self.gear_ratio = 40 / 24
        self.unit_distance = 10

        self.direction = 0

        self.x = 0
        self.y = 0

    def drive_differential(self, left_speed: float, right_speed: float):
        """
        Drive each drivetrain motor with different speeds. Positive speed indicates clockwise rotation of the motor.

        :param left_speed: speed of left motor in [-1, 1]
        :param right_speed: speed of right motor in [-1, 1]
        """

        self.left_motor.pwm(left_speed)
        self.right_motor.pwm(right_speed)

    def drive_with_speed(self, speed: float) -> None:
        """
        Drive with speed. Positive speed indicates forward motion relative to GEARS.

        :param speed: speed to drive at in [-1, 1]
        """

        self.drive_differential(speed, -speed)

    def drive_distance(self, distance: float) -> None:
        """
        Drive for a distance. Positive distance indicates forward motion relative to GEARS.

        :param distance: distance to drive to (in cm)
        """

        self.left_motor.run_for_rotations(
            distance / (2 * pi * self.wheel_radius) * self.gear_ratio,
            blocking=False,
        )
        self.right_motor.run_for_rotations(
            -distance / (2 * pi * self.wheel_radius) * self.gear_ratio,
            blocking=True,
        )

    def drive_units(self, units: float) -> None:
        """
        Drive for a number of unit distances. Positive distance indicates forward motion relative to GEARS.

        :param units: number of units to drive to
        """

        self.drive_distance(units * self.unit_distance)

    def drive_unit(self) -> None:
        """Drive one unit distance. Positive distance indicates forward motion relative to GEARS."""

        self.drive_units(1)

        match self.direction % 4:
            case 0:
                self.y += 1
            case 1:
                self.x += 1
            case 2:
                self.y -= 1
            case 3:
                self.x -= 1

    def drive_to_point_robot_relative(self, point: tuple[float, float]) -> None:
        """Drive to point relative to current position of GEARS. Positive x value indicates point to the right of the GEARS, positive y value indicates point to the front of the GEARS."""

        x, y = point[0], point[1]

        if y < 0:
            self.turn_counterclockwise()
            self.turn_counterclockwise()
            x *= -1

        self.drive_units(abs(y))

        if x > 0:
            self.turn_clockwise()
        elif x < 0:
            self.turn_counterclockwise()

        self.drive_units(abs(x))

    def drive_to_points(self, points: list[tuple[float, float]]):
        """
        Drive to a series of points. Points should be defined relative to the fixed origin point where the GEARS starts.

        :param points: list of points for GEARS to drive to
        """

        right = np.array([[0, -1], [1, 0]])
        left = np.array([[0, 1], [-1, 0]])

        for i in range(len(points) - 1):
            robot_relative_point = np.subtract(points[i + 1], points[i])

            for j in range(abs(self.direction)):
                if self.direction > 0:
                    robot_relative_point = np.matmul(right, robot_relative_point)
                elif self.direction < 0:
                    robot_relative_point = np.matmul(left, robot_relative_point)

            self.drive_to_point_robot_relative(robot_relative_point)
            print(
                f"[Drivetrain] Drove to {points[i + 1]} with vector {robot_relative_point}"
            )
            sleep(1)

    def turn_with_speed(self, speed: float) -> None:
        """
        Turn in-place with a constant speed. Positive speed indicates counterclockwise rotation.

        :param speed: speed to rotate at in [-1, 1]
        """

        self.drive_differential(-speed, -speed)

    def turn_to_angle(self, target_angle: float) -> None:
        """
        Turn in-place to a target angle. Positive angle indicates counterclockwise rotation.

        :param target_angle: angle to turn to (in degrees)
        """

        current_angle = 0
        error = target_angle - current_angle
        e_prev = 0
        dt = 0.05

        kP = 0.08
        kI = 0
        kD = 0

        while abs(error) > 0.5:
            current_angle += self.imu.angular_velocity * dt
            error = target_angle - current_angle

            p = kP * error
            i = kI * error * dt / 2
            d = kD * (error - e_prev) / dt

            effort = p + i + d

            if effort > 1:
                effort = 1
            elif effort < -1:
                effort = -1

            self.turn_with_speed(effort)
            sleep(dt)

        self.stop()

    def turn_counterclockwise(self) -> None:
        """Turn counterclockwise in-place 90 degrees."""

        self.turn_to_angle(90)
        self.direction -= 1

    def turn_clockwise(self) -> None:
        """Turn clockwise in-place 90 degrees."""

        self.turn_to_angle(-90)
        self.direction += 1

    def stop(self) -> None:
        """Stop the drivetrain."""

        self.left_motor.stop()
        self.right_motor.stop()
