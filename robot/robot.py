import wpilib
import wpilib.drive
import ctre
from magicbot import MagicRobot
from networktables import NetworkTables, NetworkTable
# from components.swerve_module import SwerveModule
# from components.swerve_drive import SwerveDrive
from components.drive_motors import drive_train

INPUT_SENSITIVITY = 0.05

# Download and install stuff on the RoboRIO after imaging
# + For packages
'''
py -3 -m robotpy_installer download-python
py -3 -m robotpy_installer install-python
py -3 -m robotpy_installer download robotpy
py -3 -m robotpy_installer install robotpy
py -3 -m robotpy_installer download robotpy[ctre]
py -3 -m robotpy_installer install robotpy[ctre]
py -3 -m robotpy_installer download robotpy[rev]
py -3 -m robotpy_installer install robotpy[rev]
py -3 -m robotpy_installer download pynetworktables
py -3 -m robotpy_installer install pynetworktables
py -3 -m pip install -U robotpy[ctre]
py -3 -m pip install robotpy[ctre]
'''

# Push code to RoboRIO (only after imaging)
'''
python robot/robot.py deploy --skip-tests
py robot/robot.py deploy --skip-tests --no-version-check
'''

INPUT_SENSITIVITY = 0.05

# NOTE: Currently Incomplete, requires rotation capabilites... on the #TODO
class SpartaBot(MagicRobot):

    drivetrain: drive_train

    def createObjects(self):
        '''Create motors and stuff here'''

        NetworkTables.initialize(server='roborio-5045-frc.local')
        self.sd: NetworkTable = NetworkTables.getTable('SmartDashboard')

        self.drive_controller: wpilib.XboxController = wpilib.XboxController(0)

        self.frontLeftDrive = ctre.WPI_TalonSRX(1)
        self.frontRightDrive = ctre.WPI_TalonSRX(3)
        self.rearLeftDrive = ctre.WPI_TalonSRX(7)
        self.rearRightDrive = ctre.WPI_TalonSRX(6)
        self.frontLeftTurn = ctre.WPI_TalonSRX(2)
        self.frontRightTurn = ctre.WPI_TalonSRX(4)
        self.rearLeftTurn = ctre.WPI_TalonSRX(8)
        self.rearRightTurn = ctre.WPI_TalonSRX(5)

        self.frontLeftModule_encoder = self.frontLeftDrive
        self.frontRightModule_encoder = self.frontRightDrive
        self.rearLeftModule_encoder = self.rearLeftDrive
        self.rearRightModule_encoder = self.rearRightDrive

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        self.sd.putValue("Mode", "Disabled")

    def teleopInit(self):
        self.drive_motors.flush

    def teleopPeriodic(self):
        # self.drivetrain.set_vector_magnitude([
        #     self.drive_controller.getLeftX(),
        #     self.drive_controller.getLeftY(),
        # ])
        # # log swerve module values
        # print("FL encoder", self.frontLeftModule_encoder.getSelectedSensorPosition())
        # print("FR encoder", self.frontRightModule_encoder.getSelectedSensorPosition())
        # print("RL encoder", self.rearLeftModule_encoder.getSelectedSensorPosition())
        # print("RR encoder", self.rearRightModule_encoder.getSelectedSensorPosition())
        # # For testing purposes // remove later
        if (abs(self.drive_controller.getLeftY())) > INPUT_SENSITIVITY or (abs(self.drive_controller.getRightX())) > INPUT_SENSITIVITY:
            self.drivetrain.set_motors(self.drive_controller.getLeftY(), self.drive_controller.getRightX())
        
        else:
            self.drivetrain.set_motors(0, 0)
        

if __name__ == '__main__':
    wpilib.run(SpartaBot)
