from buildhat import Motor


class CargoHold:
    def __init__(self) -> None:
        self.motor: Motor = Motor("C")

    def deposit(self) -> None:
        self.motor.pwm(1)
    