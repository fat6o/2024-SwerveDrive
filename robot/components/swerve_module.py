import math

import wpilib
from wpilib import WPI_TalonSRX
import ctre

from networktables import NetworkTables
from wpilib.controller import PIDController
from collections import namedtuple

ModuleConfig = namedtuple('ModuleConfig', ['sd_prefix', 'zero', 'allow_reverse'])

class SwerveModule:
    drive_motor: WPI_TalonSRX
    turn_motor: WPI_TalonSRX

    cfg: ModuleConfig

    def setup(self):
        self.sd_prefix = self.cfg.sd_prefix or 'Module'
        self.reset = self.cfg.zero or 0
        self.allow_reverse = self.cfg.allow_reverse or True

        self.requested_angle = 0
        self.requested_speed = 0

        self.pid_controller = PIDController(1.0, 0.0, 0.0)
        self.pid_controller.enableContinuousInput(0.0, 5.0) # Will set the 0 and 5 as the same point
        self.pid_controller.setTolerance(0.05, 0.05)

    def flush(self):
        self.requested_angle = self.reset
        self.requested_speed = self.reset
        self.pid_controller.reset()
    
    def set_deg(self, value):
        self.requested_angle = ((self.degree_to_ticks(value) + self.reset))

    def move(self, speed, deg):
        deg %= 360


