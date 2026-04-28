from sys import exit
from time import sleep
from subsystems import *
from sensors import *

distance_sensor = DistanceSensor()
imu = IMU()
infrared_sensor = InfraredSensor()
drivetrain = Drivetrain(imu)
cargo_hold = CargoHold()

state = "drive"
"""Current state of GEARS. Value of variable corresponds to name of state functions defined below."""


def drive():
    global state

    drivetrain.drive_unit()
    state = "sense"


def sense():
    global state

    if infrared_sensor.source_present:
        drivetrain.add_infrared(infrared_sensor.value)
        state = "turn_counterclockwise"
    # elif imu.source_present:
    #     drivetrain.add_magnet(imu.magnetic_field)
    #     state = "turn_clockwise"
    elif distance_sensor.all_clear:
        state = "deposit"
    elif distance_sensor.front_clear:
        state = "drive"
    elif distance_sensor.left_clear:
        state = "turn_counterclockwise"
    else:
        state = "turn_clockwise"


def turn_counterclockwise():
    global state

    drivetrain.turn_counterclockwise()
    state = "sense"


def turn_clockwise():
    global state

    drivetrain.turn_clockwise()
    state = "sense"


def deposit():
    drivetrain.write_output(1)
    cargo_hold.deposit()
    drivetrain.drive_units(0.5)
    exit("[Robot] GEARS mission complete")


def main():
    while True:
        distance_sensor.log()
        imu.log_magnet()
        infrared_sensor.log()

        print(state)
        eval(state)()
        drivetrain.write_output(1)
        # sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cargo_hold.deposit()
        drivetrain.stop()