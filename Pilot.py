import time

class Pilot():

    def __init__(self, healthy, rested, full, calm, focus):
        self.healthy = healthy
        self.rested = rested
        self.full = full
        self.calm = calm
        self.focus = focus

    def GetInfo(self):
        if self.healthy and self.rested and self.full and self.calm and self.focus:
            print('Check completed successfully')
        else:
            print('Error in the security process!!!!')