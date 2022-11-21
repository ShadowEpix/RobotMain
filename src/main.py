from Utilities.Robot import Robot

Reginald = Robot()


while Reginald.DoUpdate:
    if Reginald.CanUpdate:
        # do code
        Reginald.Update()