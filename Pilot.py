import time

class Pilot():

    def __init__(self, healthy, rested, full, calm, focus):
        self.healthy = healthy
        self.rested = rested
        self.full = full
        self.calm = calm
        self.focus = focus

    def CheckStatusPilot(self):
            if self.healthy and self.rested and self.full and self.calm and self.focus == str('True'):
                print('Check completed successfully')
                print('-'*100)
            else:
                print('Error in the security process!!!!')