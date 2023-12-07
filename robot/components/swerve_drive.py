from wpilib import MotorControllerGroup
import ctre
import wpilib
import wpilib.drive
from wpilib.controller import PIDController
from ctre import WPI_TalonSRX
from magicbot import MagicRobot
from networktables import NetworkTables, NetworkTable


SENSITIVITY = 0.05

SPEED_MULTIPLIER = 1
ANGLE_MULTIPLIER = 1

class drive_train:
    """NOTE: NOT a magic component, variable injection will not work here; manually instantiate"""    
    
    def setup(self):
        self.reset_speed = 0
        self.reset_angle = 0
        self.requested_speed = 0
        self.requested_angle = 0
        self.requested_strafe = 0

        self.pid_controller = PIDController(1.0, 0.0, 0.0)
        self.pid_controller.enableContinuousInput(0.0, 5.0)
        self.pid_controller.setTolerance(0.05, 0.05)
    
    def flush(self):
        self.requested_speed = self.reset_speed
        self.requested_angle = self.reset_angle
    
    def set_angle(self, angle):
        self.requested_angle = angle
    
    def set_speed(self, speed):
        self.requested_speed = speed
    
    def set_strafe(self, strafe):
        self.requested_strafe = strafe

    def move(self, speed, strafe, angle):
        self.set_angle(angle)
        self.set_speed(speed)
        self.set_strafe(strafe)
    
    


    
    def execute(self) -> None:
        self._pid_controller.reset()
        for i in self.drive_motors

