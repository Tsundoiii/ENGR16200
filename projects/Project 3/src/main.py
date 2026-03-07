from subsystems.drivetrain import Drivetrain
from sensors.distance_sensor import DistanceSensor
from sensors.ir_sensor import InfraredSensor
from time import sleep
import numpy as np

drivetrain = Drivetrain()
distance_sensor = DistanceSensor()
ir_sensor = InfraredSensor()

state = "drive"


def drive():
    global state
    
    drivetrain.drive_unit()
    state = "sense"

def sense():
    global state
    
    distance = distance_sensor.distance
    print(distance)
    
    if (distance is None or distance > 10):
        state = "drive"
    else:  
        state = "turn_left"

def turn_left():
    global state
    
    drivetrain.turn_left()
    state = "sense"
    
def turn_right():
    global state
    
    drivetrain.turn_right()
    state = "sense"
    
def task1():
    while True:
        print(state)
        eval(state)()
        
def task2():
    drivetrain.turn_to_angle(-135)
    
def task3(self, point: tuple[float, float]) -> None:
    while point != (drivetrain.x, drivetrain.y):
        x, y = point[0], point[1]
        v = (drivetrain.x - x, drivetrain.y - y)
        
        right = np.array([[0, -1], [1, 0]])
        left = np.array([[0, 1], [-1, 0]])
        
        for j in range(abs(drivetrain.direction)):
            if drivetrain.direction > 0:
                x, y = tuple(np.matmul(right, v))
            elif drivetrain.direction < 0:
                x, y = tuple(np.matmul(left, v))
  
        if y == 0:
            continue
        if y < 0:
            self.turn_left()
            self.turn_left()
            x *= -1
            
        if (abs(drivetrain.imu.getGyro()[1]) > 100) or (ir_sensor.average is not None and ir_sensor.average > 20):
            self.turn_right()
            continue
        
        self.drive_unit()

        if x == 0:
            continue
        if x > 0:
            self.turn_right()
        elif x < 0:
            self.turn_left()

        self.drive_unit()
    
def task4():
    drivetrain.drive_to_points([(0, 0), (1,2), (3, 0), (3, 2), (0, 3)])


def main():
    task1()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        drivetrain.stop()
