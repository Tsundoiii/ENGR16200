from basehat import IMUSensor
from numpy.linalg import norm


class IMU:
    """Inertial measurement unit of GEARS."""

    def __init__(self):
        """Create IMU."""

        self.sensor = IMUSensor()
        self.threshold = 50

    @property
    def angular_velocity(self) -> float:
        """Angular velocity of GEARS."""

        return self.sensor.getGyro()[2]

    @property
    def x(self) -> float:
        return self.sensor.getMag()[0]
    
    @property
    def y(self) -> float:
        return self.sensor.getMag()[1]

    @property
    def magnetic_field(self) -> float:
        """Magnitude of magnetic field (in mT)."""

        return norm(self.sensor.getMag()[:2])
    
    @property
    def source_present(self) -> bool:
        return self.magnetic_field > self.threshold

    @property
    def source_direction(self) -> tuple[int, int]:
        x, y, _  = self.sensor.getMag()

        if max(x, y, key=abs) == y:
            return (0, 1)
        elif x > 0:
            return (-1, 0)
        else:
            return (1, 0)

    def log_angle(self) -> None:
        """Log angular velocity (in deg / ) of GEARS."""
        
        print(f"[IMU] | (Angle) {self.angular_velocity} deg / s")

    def log_magnet(self) -> None:
        print(f"[IMU] | Field: {self.magnetic_field} | (x) {self.x} | (y) {self.y} | Present: {self.source_present}")
