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
        #time.sleep(2)
        print('I am your on-board computer')
        #time.sleep(5)
        print('Today is: {}'.format(time.strftime("%d/%m/%Y, %H:%M", time.localtime())))
        #time.sleep(4)
        print('We are going to {}'.format(self.random_direction()))
        #time.sleep(2)
        print("Today's weather is: {}".format(self.random_weather()))
        #time.sleep(3)
        print('Lets prepare you for the flight, for this purpose I have to ask you a few questions')
        #time.sleep(5)
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
                #time.sleep(2)
                print("Success!!!")
                print('-' * 100)
                #time.sleep(2)
                print('Now I have to ask you about the technical condition of the aircraft')
            elif all([not i for i in inputsPilot]):
                print("Error: wrong values!!!")
            else:
                print("Error: Security check is failed")
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
                #time.sleep(2)
                print("Success!!!")
                print('-' * 100)
            elif all([not i for i in inputsAircraft]):
                print("Error: wrong values!!!")
            else:
                print("Error: Security check failed")
                raise SystemExit

            if all(inputsAircraft):
                self.LaunchSequence_info()
            else:
                return inputsAircraft

        except KeyboardInterrupt:
            print("Program interrupted by user.")

    def LaunchSequence_info(self):
        options = {
            "1": "Air traffic control tower",
            "2": "Passengers",
            "3": "Second pilot"
        }
        current_answer = ["Air traffic control tower", "Passengers"]
        user_choice = input(
            "We want to ask for permission to take off, who do we need to notify?\n1. Air traffic control tower\n2. "
            "Passengers\n3. Second pilot\nSelect the option: ").strip().lower()

        if user_choice == "1 2" or user_choice == "2 1":
            time.sleep(2)
            print("Yes sir - I am informing the air traffic control tower and passengers of my intention to take off.")
            print("-" * 100)
            time.sleep(2)
            self.LaunchSequence_collisionLights()
        elif user_choice in options:
            if options[user_choice] in current_answer:
                time.sleep(2)
                print("Yes sir - I am informing the", options[user_choice], "of my intention to take off, But we need "
                                                                            "to inform someone else too")
                print("-" * 100)
                time.sleep(2)
                print("Let's try again")
                self.LaunchSequence_info()
            else:
                print("Wrong answer!!!")
                time.sleep(2)
                print("Let's try again")
                self.LaunchSequence_info()
        else:
            print("Incorrect selection option!!!")
            time.sleep(2)
            print("Let's try again")
            self.LaunchSequence_info()

    def LaunchSequence_collisionLights(self):
        options = {
            "1": "Including engines",
            "2": "Turn on blinking collision lights",
            "3": "Hide the landing gear of the aircraft"
        }

        current_answer = "Turn on blinking collision lights"
        user_choice = input(
            "We need to let everyone around us know that we are starting the launch sequence. What do we need to do?\n1. "
            "Including engines\n2. Turn on blinking collision lights\n3. Hide the landing gear of the aircraft"
            "\nSelect the option: "
        ).strip().lower()

        if user_choice in options:
            if options[user_choice] == current_answer:
                time.sleep(2)
                print("That's right, I turn on the collision lights. They appear to be blinking. ")
                print('-'*100)
                time.sleep(2)
                self.LaunchSequence_engines()
            else:
                print("Wrong answer!!!")
                time.sleep(2)
                print("Let's try again")
                print('*'*100)
                time.sleep(2)
                self.LaunchSequence_collisionLights()
        else:
            print("Incorrect selection option!!!")
            time.sleep(2)
            print("Let's try again")
            print('*' * 100)
            time.sleep(2)
            self.LaunchSequence_collisionLights()


    def LaunchSequence_engines(self):
        options = {
            "1": "Refuel the aircraft",
            "2": "Open the luggage compartment",
            "3": "Turn on the engines one at a time"
        }

        current_answer = "Turn on the engines one at a time"
        user_choice = input(
            "We need to generate the thrust needed to get the plane up. What do we need to do?\n1. "
            "Refuel the aircraft\n2. Open the luggage compartment\n3. Turn on the engines one at a time\n"
            "Select the option: ").strip().lower()

        if user_choice in options:
            if options[user_choice] == current_answer:
                time.sleep(2)
                print("Of course, I'm starting to run engine #1")
                time.sleep(4)
                print("Engine #1 has warmed up, I am starting to start engine #2")
                print("-"*100)
                time.sleep(4)
                print("Pilot, we are now taxiing...")
                time.sleep(4)
                print("We are gaining launch speed...")

            else:
                print("Wrong answer!!!")
                time.sleep(2)
                print("Let's try again")
                print('*' * 100)
                time.sleep(2)
                self.LaunchSequence_engines()
        else:
            print("Incorrect selection option!!!")
            time.sleep(2)
            print("Let's try again")
            print('*' * 100)
            time.sleep(2)
            self.LaunchSequence_engines()






