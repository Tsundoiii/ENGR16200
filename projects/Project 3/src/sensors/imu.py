from basehat import IMUSensor
from numpy.linalg import norm


class IMU:
    """Inertial measurement unit of GEARS."""

    def __init__(self):
        """Create IMU."""

        self.sensor = IMUSensor()

    @property
    def angle(self) -> float:
        pass

    @property
    def magnetic_field(self) -> float:
        """Magnitude of magnetic field (in mT)."""

        return norm(self.sensor.getMag())
