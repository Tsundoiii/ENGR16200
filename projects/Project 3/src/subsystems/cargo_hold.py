from buildhat import Motor

class CargoHold:
    def __init__(self) -> None:
        self.motor: Motor = Motor("B")

    def deposit(self) -> None:
        self.motor.pwm(1)
        #self.motor.run_for_seconds(3)
    