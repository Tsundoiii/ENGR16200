from basehat import IMUSensor
from numpy.linalg import norm


class IMU:
    """Inertial measurement unit of GEARS."""

    def __init__(self):
        """Create IMU."""

        self.sensor = IMUSensor()

    @property
    def angular_velocity(self) -> float:
        """Angular velocity of GEARS."""

        return self.sensor.getGyro()[2]

    @property
    def magnetic_field(self) -> float:
        """Magnitude of magnetic field (in mT)."""

        return norm(self.sensor.getMag())

    def log(self) -> None:
        """Log angular velocity (in deg / ) of GEARS."""
        
        print(f"[IMU] | (Angle) {self.angular_velocity} deg / s")
