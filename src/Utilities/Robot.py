from vex import *
import enum

class Buttons(enum):
    

#########

class Robot():
    def __init__(self) -> None:
        self.Name = "Reginald"
        self.SpeedMultiplier = 1
        self.Speed = 10
        
        self.CanUpdate = True
        self.DoUpdate = True

        self.Brain = Brain()
        self.Controller = Controller(PRIMARY)
        self.Motors = {
            "DriveMotorL":Motor(Ports.PORT1, GearSetting.RATIO_18_1, False),
            "DriveMotorR":Motor(Ports.PORT10, GearSetting.RATIO_18_1, True),
            "ArmMotor":Motor(Ports.PORT8, GearSetting.RATIO_18_1, False),
            "ClawMotor":Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
        }
        
    def Update(self):
        self.Motors["DriveMotorL"].set_velocity(self.Controller.axis3.position(), PERCENT)
        self.Motors["DriveMotorR"].set_velocity(self.Controller.axis2.position(), PERCENT)

        self.Motors["DriveMotorL"].spin(FORWARD)
        self.Motors["DriveMotorR"].spin(FORWARD)

    def Exit(self):
        self.CanUpdate = False
        self.DoUpdate = False
    
    def Yield(self, Yield):
        self.CanUpdate = Yield