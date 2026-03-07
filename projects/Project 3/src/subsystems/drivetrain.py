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

        :param left_speed: speed of left motor
        :param right_speed: speed of right motor
        """

        self.left_motor.pwm(left_speed)
        self.right_motor.pwm(right_speed)

    def drive_with_speed(self, speed: float) -> None:
        """
        Drive drivetrain with a speed. Positive speed indicates forward motion relative to robot.

        :param speed: speed to drive at
        """

        self.drive_differential(speed, -speed)

    def drive_distance(self, distance: float) -> None:
        """
        Drive drivetrain for a distance. Positive distance indicates forward motion relative to robot.

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
        Drive drivetrain for a number of unit distances. Positive distance indicates forward motion relative to robot.

        :param units: number of units to drive to
        """

        self.drive_distance(units * self.unit_distance)
        
    def drive_unit(self) -> None:
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
        x, y = point[0], point[1]
  
        if y < 0:
            self.turn_left()
            self.turn_left()
            x *= -1
        
        self.drive_units(abs(y))

        if x > 0:
            self.turn_right()
        elif x < 0:
            self.turn_left()

        self.drive_units(abs(x))

    def drive_to_points(self, points: list[tuple[float, float]]):
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
            print(f"Drove to {points[i+1]} with vector {robot_relative_point}")
            sleep(5)
                    
    def turn_with_speed(self, speed: float) -> None:
        self.drive_differential(-speed, -speed)

    def turn_to_angle(self, target_angle: float):
        current_angle = 0
        error = target_angle - current_angle
        e_prev = 0
        dt = 0.05

        kP = 0.08
        kI = 0
        kD = 0

        while abs(error) > 1:
            current_angle += self.imu.getGyro()[2] * dt
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

    def turn_right(self):
        self.turn_to_angle(-90)
        self.direction += 1
        print(f"Turn right k = {self.direction}")

    def turn_left(self):
        self.turn_to_angle(90)
        self.direction -= 1
        print(f"Turn left k = {self.direction}")

    def stop(self) -> None:
        """Stop the drivetrain."""

        self.left_motor.stop()
        self.right_motor.stop()
