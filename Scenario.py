import time
import random
from Pilot import Pilot
from Aircraft import Aircraft

class Scenario(Pilot, Aircraft):

    directions = ["Warsaw", "Baghdad", "Tokyo", "Sydney"]
    weather = ["Storm", "Sunny"]


    def __init__(self, healthy, rested, full, calm, focus, fuel, engines, lights, collisionLights, rudders, hydraulicsSystem):
        Pilot.__init__(self, healthy, rested, full, calm, focus)
        Aircraft.__init__(self, fuel, engines, lights, collisionLights, rudders, hydraulicsSystem)
        self.scenario_inputsPilot = []
        self.scenario_inputsAircraft = []


    def RunScenario(self):
        print('Hi')
        time.sleep(2)
        print('I am your on-board computer')
        time.sleep(5)
        print('Today is {}'.format(time.strftime("%m/%d/%Y, %H:%M", time.localtime())))
        time.sleep(4)
        print('We are going to {}'.format(self.random_direction()))
        time.sleep(2)
        print('The weather for today is {}'.format(self.random_weather()))
        time.sleep(3)
        print('Lets prepare you for the flight, for this purpose I have to ask you a few questions')
        time.sleep(5)
        print('Remember, the answers are only True or False')

        self.SetStatusPilot()

    def random_direction(self):
        return random.choice(self.directions)

    def random_weather(self):
        return random.choice(self.weather)

    def SetStatusPilot(self):
        self.healthy = input('Do you feel healthy? (True/False) ')
        self.rested = input('Do you feel rested? (True/False) ')
        self.full = input('Do you feel full? (True/False) ')
        self.calm = input('Are you calm? (True/False) ')
        self.focus = input('Are you focused? (True/False) ')

        inputsPilot = [self.healthy.lower() == 'true', self.rested.lower() == 'true', self.full.lower() == 'true',\
                       self.calm.lower() == 'true',
                       self.focus.lower() == 'true']

        try:
            if all(inputsPilot):
                print('Wait for the verification process...')
                time.sleep(2)
                print("Success!!!")
                print('-' * 100)
                time.sleep(2)
                print('Now I have to ask you about the technical condition of the aircraft')
            elif all([not i for i in inputsPilot]):
                print("Error!!!")
            else:
                print("Error: wrong values!!!")
                raise SystemExit

            if all(inputsPilot):
                self.SetStatusAircraft()
            else:
                return inputsPilot

        except KeyboardInterrupt:
            print("Program interrupted by user.")


    def SetStatusAircraft(self):
        self.fuel = input('Is the fuel tank dueled? (True/False)')
        self.engines = input('Are all engines operational? (True/False)')
        self.lights = input('Do the lights work? (True/False)')
        self.collisionLights = input('Do the collision lights work? (True/False)')
        self.rudders = input('Are the controllers working? (True/False)')
        self.hydraulicsSystem = input('Are the hydraulic systems working well? (True/False)')

        inputsAircraft = [self.fuel.lower() == 'true', self.engines.lower() == 'true', self.lights.lower() == 'true',\
                          self.collisionLights.lower() == 'true', self.rudders.lower() == 'true',\
                          self.hydraulicsSystem.lower() == 'true']


        try:
            if all(inputsAircraft):
                print('Wait for the verification process...')
                time.sleep(2)
                print("Success!!!")
                print('-' * 100)
            elif all([not i for i in inputsAircraft]):
                print('Error!!!')
            else:
                print("Error: wrong values!!!")
                raise SystemExit

            if all(inputsAircraft):
                pass
            else:
                return inputsAircraft

        except KeyboardInterrupt:
            print("Program interrupted by user.")