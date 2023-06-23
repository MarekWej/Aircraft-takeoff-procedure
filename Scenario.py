import time
from Pilot import Pilot

class Scenario(Pilot):

    def __init__(self, healthy, rested, full, calm, focus):
        super().__init__(healthy, rested, full, calm, focus)

    def RunScenario(self):
        print('Hi')
        time.sleep(2)
        print('I am your on-board computer')
        time.sleep(5)
        print('Today is {}'.format(time.strftime("%m/%d/%Y, %H:%M", time.localtime())))
        time.sleep(3)
        print('Lets prepare you for the flight, for this purpose I have to ask you a few questions')
        time.sleep(5)
        print('Remember, the answers are only True or False')

        self.SetStatus()

        self.GetInfo()

    def SetStatus(self):
        self.healthy = bool(input('Do you feel healthy?'))
        self.rested = bool(input('Do you feel rested?'))
        self.full = bool(input('Do you feel full?'))
        self.calm = bool(input('Are you calm?'))
        self.focus = bool(input('Are you focused?'))

