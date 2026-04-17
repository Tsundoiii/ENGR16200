from sys import exit
from subsystems.drivetrain import Drivetrain
from subsystems.cargo_hold import CargoHold
from sensors.distance_sensor import DistanceSensor
from sensors.imu import IMU
from sensors.ir_sensor import InfraredSensor
import numpy as np

drivetrain = Drivetrain(IMU())
cargo_hold = CargoHold()
distance_sensor = DistanceSensor()
ir_sensor = InfraredSensor()

state = "drive"
"""Current state of GEARS. Value of variable corresponds to name of state functions defined below."""


def drive():
    global state

    drivetrain.drive_unit()
    state = "sense"


def sense():
    global state

    # if distance_sensor.all_clear:
        # state = "deposit"
    if distance_sensor.front_clear:
        state = "drive"
    elif distance_sensor.right_clear:
        state = "turn_clockwise"
    else:
        state = "turn_counterclockwise"


def turn_counterclockwise():
    global state

    drivetrain.turn_counterclockwise()
    state = "sense"


def turn_clockwise():
    global state

    drivetrain.turn_clockwise()
    state = "sense"

def deposit():
    cargo_hold.deposit()
    drivetrain.write_map(1)
    exit("[Robot] GEARS mission complete")

def task12():
    main()

def task34():
    drivetrain.drive_to_points([(1,2), (3, 2), (0, 1)])

def task56():
    main()

def main():
    while True:
        eval(state)()


if __name__ == "__main__":
    try:
        task34()
    except KeyboardInterrupt:
        drivetrain.stop()
        drivetrain.write_map(1)
