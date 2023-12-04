from wpilib import MotorControllerGroup
import ctre
import wpilib
import wpilib.drive
from ctre import WPI_TalonSRX
from magicbot import MagicRobot
from networktables import NetworkTables, NetworkTable


SENSITIVITY = 0.05

SPEED_MULTIPLIER = 1
ANGLE_MULTIPLIER = 1

class drive_train:
    """NOTE: NOT a magic component, variable injection will not work here; manually instantiate"""
    frontLeftDrive: WPI_TalonSRX
    frontRightDrive: WPI_TalonSRX
    rearLeftDrive: WPI_TalonSRX
    rearRightDrive: WPI_TalonSRX
    frontLeftTurn: WPI_TalonSRX
    frontRightTurn: WPI_TalonSRX
    rearLeftTurn: WPI_TalonSRX
    rearRightTurn: WPI_TalonSRX
    
    def setup(self):
        self.speed = 0
        self.angle = 0

        
    def set_motors(self, speed: float, angle: float):
        self.speed = speed
        self.angle = angle

    
    def execute(self) -> None:
        self.frontLeftDrive.set(self.speed)
        self.frontRightDrive.set(self.speed)
        self.rearLeftDrive.set(self.speed)
        self.rearRightDrive.set(self.speed)
        self.frontLeftTurn.set(self.angle)
        self.frontRightTurn.set(self.angle)
        self.rearLeftTurn.set(self.angle)
        self.rearRightTurn.set(self.angle)


