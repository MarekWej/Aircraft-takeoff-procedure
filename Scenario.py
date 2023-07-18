import sys
import os
import time
import random

from Pilot import Pilot
from Aircraft import Aircraft
from tkinter import *

class Scenario(Pilot, Aircraft):

    directions = ["Warsaw", "Baghdad", "Tokyo", "Sydney"]
    weather = ["Storm", "Sunny"]


    def __init__(self, healthy, rested, full, calm, focus, fuel, engines, lights, collisionLights, rudders, hydraulicsSystem):
        Pilot.__init__(self, healthy, rested, full, calm, focus)
        Aircraft.__init__(self, fuel, engines, lights, collisionLights, rudders, hydraulicsSystem)
        self.scenario_inputsPilot = []
        self.scenario_inputsAircraft = []
        self.city = self.random_direction()


    def RunScenario(self):
        print('Hi')
        #time.sleep(2)
        print('I am your on-board computer')
        #time.sleep(5)
        print('Today is: {}'.format(time.strftime("%d/%m/%Y, %H:%M", time.localtime())))
        #time.sleep(4)
        print('We are going to {}'.format(self.city))
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
        root = Tk()
        root.title("Pilot status")
        root.geometry("600x450")

        status_frame = Frame(root)
        status_frame.pack(pady=20)

        questions = ["Do you feel healthy?", "Do you feel rested?", "Do you feel full?", "Are you calm?",
                     "Are you focused?"]
        answers = []
        for i in range(len(questions)):
            var = IntVar()
            var.set(-1)  # Initial value -1, so that no option is selected
            question_label = Label(status_frame, text=questions[i])
            question_label.pack()
            yes_option = Radiobutton(status_frame, text="Yes", variable=var, value=1)
            yes_option.pack()
            no_option = Radiobutton(status_frame, text="No", variable=var, value=0)
            no_option.pack()
            answers.append(var)

        def submit_status():
            self.healthy = answers[0].get() == 1
            self.rested = answers[1].get() == 1
            self.full = answers[2].get() == 1
            self.calm = answers[3].get() == 1
            self.focus = answers[4].get() == 1

            if all(answer.get() != 0 for answer in answers):
                print('Wait for the verification process...')
                time.sleep(2)
                print("Success!!!")
                print('-' * 100)
                time.sleep(2)
                print('Now I have to ask you about the technical condition of the aircraft')
                root.destroy()
                self.SetStatusAircraft()
            else:
                print("Error: Security check failed")
                root.destroy()
                time.sleep(1)
                self.SetStatusPilot()

        submit_button = Button(root, text="Submit", command=submit_status)
        submit_button.pack()

        root.mainloop()

    def SetStatusAircraft(self):
        root = Tk()
        root.title("Aircraft status")
        root.geometry("600x550")

        status_frame = Frame(root)
        status_frame.pack(pady=20)

        questions = ["Is the fuel tank fueled?", "Are all engines operational?", "Do the lights work?",
                     "Do the collision lights work?",
                     "Are the controllers working?", "Are the hydraulic systems working well?"]
        answers = []
        for i in range(len(questions)):
            var = IntVar()
            var.set(-1)
            question_label = Label(status_frame, text=questions[i])
            question_label.pack()
            yes_option = Radiobutton(status_frame, text="Yes", variable=var, value= 1)
            yes_option.pack()
            no_option = Radiobutton(status_frame, text="No", variable=var, value= 0)
            no_option.pack()
            answers.append(var)

        def submit_status():
            self.fuel = answers[0].get() == 1
            self.engines = answers[1].get() == 1
            self.lights = answers[2].get() == 1
            self.collisionLights = answers[3].get() == 1
            self.rudders = answers[4].get() == 1
            self.hydraulicsSystem = answers[5].get() == 1

            if all(answer.get() != 0 for answer in answers):
                print('Wait for the verification process...')
                time.sleep(2)
                print("Success!!!")
                print('-' * 100)
                root.destroy()
                self.LaunchSequence_info()
            else:
                print("Error: Security check failed")
                root.destroy()
                time.sleep(1)
                self.SetStatusAircraft()

        submit_button = Button(root, text="Submit", command=submit_status)
        submit_button.pack()

        root.mainloop()

    def LaunchSequence_info(self):
        root = Tk()
        root.title("Launch sequence info")
        root.geometry("400x300")

        info_frame = Frame(root)
        info_frame.pack(pady=20)

        question_label = Label(info_frame, text="We want to ask for permission to take off, who do we need to notify?")
        question_label.pack()

        options = {
            "1": "Air traffic control tower",
            "2": "Passengers",
            "3": "Second pilot"
        }
        current_answer = ["Air traffic control tower", "Passengers"]

        var1 = BooleanVar()
        option1 = Checkbutton(info_frame, text=options["1"], variable=var1)
        option1.pack()

        var2 = BooleanVar()
        option2 = Checkbutton(info_frame, text=options["2"], variable=var2)
        option2.pack()

        var3 = BooleanVar()
        option3 = Checkbutton(info_frame, text=options["3"], variable=var3)
        option3.pack()

        def submit_info():
            choice = []
            if var1.get():
                choice.append(options["1"])
            if var2.get():
                choice.append(options["2"])
            if var3.get():
                choice.append(options["3"])

            if choice == current_answer:
                print(
                    "Yes sir - I am informing the air traffic control tower and passengers of my intention to take off.")
                print("-" * 100)
                root.destroy()
                self.LaunchSequence_collisionLights()
            elif choice:
                print("Wrong answer!!!")
                print("Let's try again")
                print('*' * 100)
            else:
                print("No option selected!!!")
                print("Let's try again")
                print('*' * 100)

        submit_button = Button(root, text="Submit", command=submit_info)
        submit_button.pack()

        root.mainloop()


    def LaunchSequence_collisionLights(self):
        root = Tk()
        root.title("Launch sequence - collision lights")
        root.geometry("400x300")

        info_frame = Frame(root)
        info_frame.pack(pady=20)

        question_label = Label(info_frame, text="We need to let everyone around us know that we are starting the launch "
                                                "sequence. What do we need to do?")
        question_label.pack()

        options = {
            "1": "Including engines",
            "2": "Turn on blinking collision lights",
            "3": "Hide the landing gear of the aircraft"
        }

        current_answer = ["Turn on blinking collision lights"]

        var1 = BooleanVar()
        options1 = Checkbutton(info_frame, text=options["1"], variable=var1)
        options1.pack()

        var2 = BooleanVar()
        options2 = Checkbutton(info_frame, text=options["2"], variable=var2)
        options2.pack()

        var3 = BooleanVar()
        options1 = Checkbutton(info_frame, text=options["3"], variable=var3)
        options1.pack()

        def submit_info():
            choice = []

            if var1.get():
                choice.append(options["1"])
            if var2.get():
                choice.append(options["2"])
            if var3.get():
                choice.append(options["3"])

            if choice == current_answer:
                    #time.sleep(2)
                    print("That's right, I turn on the collision lights. They appear to be blinking. ")
                    print('-'*100)
                    root.destroy()
                    #time.sleep(2)
                    self.LaunchSequence_engines()
            elif choice:
                    print("Wrong answer!!!")
                    #time.sleep(2)
                    print("Let's try again")
                    print('*'*100)
                    root.destroy()
                    #time.sleep(2)
                    self.LaunchSequence_collisionLights()
            else:
                print("Incorrect selection option!!!")
                #time.sleep(2)
                print("Let's try again")
                print('*' * 100)
                #time.sleep(2)
                self.LaunchSequence_collisionLights()

        submit_button = Button(root, text="Submit", command= submit_info)
        submit_button.pack()


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
                #time.sleep(2)
                print("Of course, I'm starting to run engine #1")
                #time.sleep(4)
                print("Engine #1 has warmed up, I am starting to start engine #2")
                #time.sleep(2)
                print("-"*100)
                #time.sleep(4)
                print("Pilot, we are now taxiing...")
                #time.sleep(4)
                print("We are gaining launch speed...")
                #time.sleep(3)
                print("Pilot, the plane's takeoff was successful, I'm taking a course to {}".format(self.city))
                print('-'*100)
                print('(AT THIS STAGE AN ERROR COUNTER IS INTRODUCED, THINK TWICE BEFORE GIVING YOUR ANSWER)')
                print('-'*100)
                self.Directions()

            else:
                print("Wrong answer!!!")
                #time.sleep(2)
                print("Let's try again")
                print('*' * 100)
                #time.sleep(2)
                self.LaunchSequence_engines()
        else:
            print("Incorrect selection option!!!")
            #time.sleep(2)
            print("Let's try again")
            print('*' * 100)
            #time.sleep(2)
            self.LaunchSequence_engines()

    def Directions(self):
        continue_execution = True
        error_count = 0

        # Direction - Tokyo
        while continue_execution:
            if self.city == 'Tokyo':
                options = {
                    "1": "Notify the flight control station",
                    "2": "Notify passengers of the problem",
                    "3": "Create a panic"
                }

                current_answer = ["Notify the flight control station", "Notify passengers of the problem"]
                user_choice = input(
                    "It seems that something is wrong with engine #1, its power has dropped. We are almost there, "
                    "above the city. What should we do?\n1. Notify the flight control station"
                    "\n2. Notify passengers of the problem\n3. Increase the power of engine #2\n"
                    "Select the option: ").strip().lower()

                if user_choice == "1 2" or user_choice == "2 1":
                    print(
                        "Yes, sir. I am notifying the flight control station and passengers of the problem that has arisen.")
                    print('-' * 100)
                    continue_execution = False

                elif user_choice in options:
                    if options[user_choice] in current_answer:
                        print('-' * 100)
                        print("Executes:", options[user_choice], "but we need to do something else.")
                        error_count += 1
                        print('-' * 100)
                        print("Wrong answers = {}/3".format(error_count))
                        print('-' * 100)
                        print("Let's try again.")
                        print('-' * 100)
                    else:
                        error_count += 1
                        print("Wrong answers = {}/3".format(error_count))
                        print('-' * 100)

                        if error_count >= 3:
                            print("You have exceeded the maximum number of incorrect answers. Exiting.")
                            print("Wrong answers = {}/3".format(error_count))
                            return
                        print("Let's try again.")
                        time.sleep(2)
                else:
                    error_count += 1
                    print('-' * 100)
                    print("Wrong answers = {}/3".format(error_count))
                    print('-' * 100)
                    if error_count >= 3:
                        print("You have exceeded the maximum number of incorrect answers. Exiting.")
                        print("Wrong answers = {}/3".format(error_count))
                        return
                    print("Incorrect selection option!!!")
                    print("Let's try again.")
                    time.sleep(2)

            # Direction - Warsaw
            elif self.city == "Warsaw":
                options = {
                    "1": "Lock the cockpit door and continue flying to the designated destination",
                    "2": "Neutralize the terrorists at all costs",
                    "3": "Negotiate with terrorists"
                }
                current_answer = "Lock the cockpit door and continue flying to the designated destination"
                user_choice = input(
                    "Passengers started shouting that there were terrorists on the plane. What should we do?\n1. "
                    "Lock the cockpit door and continue flying to the designated destination\n2. "
                    "Neutralize the terrorists at all costs\n3. Negotiate with terrorists\nSelect the option: ").strip()

                if user_choice in options:
                    if options[user_choice] == current_answer:
                        print("That's right, pilot! Close the door immediately!!!")
                        print('-' * 100)
                        break
                    else:
                        error_count += 1
                        print('-' * 100)
                        print("Wrong answers = {}/3".format(error_count))
                        print('-' * 100)
                        if error_count >= 3:
                            print("You have exceeded the maximum number of incorrect answers. Exiting.")
                            return
                        print("Let's try again.")
                        print('-' * 100)
                else:
                    error_count += 1
                    print('-' * 100)
                    print("Wrong answers = {}/3".format(error_count))
                    print('-' * 100)
                    if error_count >= 3:
                        print("You have exceeded the maximum number of incorrect answers. Exiting.")
                        print("Wrong answers = {}/3".format(error_count))
                        return
                    print("Incorrect selection option!!!")
                    print("Let's try again.")
                    print('-' * 100)

            # Direction - Sydney
            elif self.city == 'Sydney':
                options = {
                    "1": "Perform a routine landing",
                    "2": "Initiate emergency landing procedures",
                    "3": "Request assistance from air traffic control"
                }
                current_answer = "Perform a routine landing"
                user_choice = input(
                    "The weather conditions have worsened unexpectedly. What should we do?\n1. Perform a routine landing"
                    "\n2. Initiate emergency landing procedures\n3. Request assistance from air traffic control"
                    "\nSelect the option: ").strip()

                if user_choice in options:
                    if options[user_choice] == current_answer:
                        print("You made the correct decision. Prepare for landing!")
                        print('-' * 100)
                        break
                    else:
                        error_count += 1
                        print('-' * 100)
                        print("Wrong answers = {}/3".format(error_count))
                        print('-' * 100)
                        if error_count >= 3:
                            print("You have exceeded the maximum number of incorrect answers. Exiting.")
                            return
                        print("Let's try again.")
                        print('-' * 100)
                else:
                    error_count += 1
                    print('-' * 100)
                    print("Wrong answers = {}/3".format(error_count))
                    print('-' * 100)
                    if error_count >= 3:
                        print("You have exceeded the maximum number of incorrect answers. Exiting.")
                        print("Wrong answers = {}/3".format(error_count))
                        return
                    print("Incorrect selection option!!!")
                    print("Let's try again.")
                    print('-' * 100)

            # Direction - "Baghdad"
            elif self.city == "Baghdad":
                options = {
                    "1": "We're landing on the water, and notify the air traffic control tower of the decision taken",
                    "2": "We ignore the pilots calculations and land according to the computer's calculations at the "
                         "nearest airport",
                    "3": "We inform passengers that we will all die"
               }
                current_answer = "We're landing on the water, and notify the air traffic control tower of the decision " \
                                 "taken"

                user_choice = input("There was a fuel leak, because of this, all the propellers stopped working. "
                                    "The computer calculated that the altitude was sufficient to reach the nearest "
                                    "airport in an emergency, but the pilot's calculations show that we will not reach "
                                    "it and will collide with buildings. What should we do?\n1. We're landing on the "
                                    "water, and notify the air traffic control tower of the decision taken\n2. We ignore "
                                    "the pilots calculations and land according to the computer's calculations at the "
                                    "nearest airport\n3. We inform passengers that we will all die\nSelect the option: "
                                    ).strip()

                if user_choice in options:
                    if options[user_choice] == current_answer:
                        print("You made the correct decision. Prepare for landing!")
                        print('-' * 100)
                        break
                    else:
                        error_count += 1
                        print('-' * 100)
                        print("Wrong answers = {}/3".format(error_count))
                        print('-' * 100)
                        if error_count >= 3:
                            print("You have exceeded the maximum number of incorrect answers. Exiting.")
                            return
                        print("Let's try again.")
                        print('-' * 100)
                else:
                    error_count += 1
                    print('-' * 100)
                    print("Wrong answers = {}/3".format(error_count))
                    print('-' * 100)
                    if error_count >= 3:
                        print("You have exceeded the maximum number of incorrect answers. Exiting.")
                        print("Wrong answers = {}/3".format(error_count))
                        return
                    print("Incorrect selection option!!!")
                    print("Let's try again.")
                    print('-' * 100)










