from basehat import IMUSensor
from numpy.linalg import norm


class IMU:
    """Inertial measurement unit of GEARS."""

    def __init__(self):
        """Create IMU."""

        self.sensor = IMUSensor()

    def angle(self) -> float:
        return self.sensor.getGyro()[2]

    @property
    def magnetic_field(self) -> float:
        """Magnitude of magnetic field (in mT)."""

        return norm(self.sensor.getMag())

    def log(self) -> str:
        return f"[IMU] (Angle) {self.angle()} deg / s"
