import time
from Pilot import Pilot
from Aircraft import Aircraft

class Scenario(Pilot,Aircraft):

    def __init__(self, healthy, rested, full, calm, focus):
        super().__init__(healthy, rested, full, calm, focus)
        self.healthy = healthy
        self.rested = rested
        self.full = full
        self.calm = calm
        self.focus = focus
        self.scenario_inputs = []

    def RunScenario(self):
        print('Hi')
        #time.sleep(2)
        print('I am your on-board computer')
        #time.sleep(5)
        print('Today is {}'.format(time.strftime("%m/%d/%Y, %H:%M", time.localtime())))
        #time.sleep(3)
        print('Lets prepare you for the flight, for this purpose I have to ask you a few questions')
        #time.sleep(5)
        print('Remember, the answers are only True or False')

        self.SetStatusPilot()

        self.CheckStatusPilot()

    def SetStatusPilot(self):
        self.healthy = input('Do you feel healthy? (True/False) ')
        self.rested = input('Do you feel rested? (True/False) ')
        self.full = input('Do you feel full? (True/False) ')
        self.calm = input('Are you calm? (True/False) ')
        self.focus = input('Are you focused? (True/False) ')

        inputs = [self.healthy.lower() == 'true', self.rested.lower() == 'true', self.full.lower() == 'true',\
                  self.calm.lower() == 'true',
                  self.focus.lower() == 'true']

        try:
            if all(inputs):
                print("Success")
            elif all([not i for i in inputs]):
                print("Error")
            else:
                print("Error: wrong values")
        except KeyboardInterrupt:
            print("Program interrupted by user.")

        return inputs
