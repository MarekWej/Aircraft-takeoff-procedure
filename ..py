    def Directions(self):

        error_count = 0
        continue_execution = True

        # Direction - Tokyo
        while continue_execution and self.city == 'Tokyo':
            options = {
                "1": "Notify the flight control station",
                "2": "Notify passengers of the problem",
                "3": "Increase the power of engine #2"
            }
            current_answer = ["Notify the flight control station", "Notify passengers of the problem"]

            user_choice = input(
                "It seems that something is wrong with engine #1, its power has dropped. We are almost there, "
                "above the city. What should we do?\n1. Notify the flight control station\n2. Notify passengers of the problem\n3. Increase the power of engine #2\n")

            if user_choice in current_answer:
                print("It was a good choice. We can land on the second engine. We will be there in a moment.")
                print("We landed safely at Tokyo Airport.")
                print("-" * 100)
                continue_execution = False
            elif user_choice in options.values():
                error_count += 1
                if error_count >= 3:
                    print("Wrong answer!!!")
                    print("Let's try again")
                    print('*' * 100)
                    continue_execution = False
                else:
                    print("Error! But you have more attempts ({}/3)".format(3 - error_count))
            else:
                print("Incorrect selection option!!!")
                print("Let's try again")
                print('*' * 100)

        continue_execution = True

        # Direction - Sydney
        while continue_execution and self.city == 'Sydney':
            options = {
                "1": "Fly lower and look for the airport visually",
                "2": "Use the aircraft's navigation system",
                "3": "Increase engine power"
            }
            current_answer = ["Fly lower and look for the airport visually", "Use the aircraft's navigation system"]

            user_choice = input(
                "We are almost at our destination. However, a thick layer of clouds is obscuring our view. "
                "What should we do?\n1. Fly lower and look for the airport visually\n2. Use the aircraft's navigation system\n3. Increase engine power\n")

            if user_choice in current_answer:
                print("Good decision. We are landing at Sydney Airport.")
                print("-" * 100)
                continue_execution = False
            elif user_choice in options.values():
                error_count += 1
                if error_count >= 3:
                    print("Wrong answer!!!")
                    print("Let's try again")
                    print('*' * 100)
                    continue_execution = False
                else:
                    print("Error! But you have more attempts ({}/3)".format(3 - error_count))
            else:
                print("Incorrect selection option!!!")
                print("Let's try again")
                print('*' * 100)

        continue_execution = True

        # Direction - Warsaw
        while continue_execution and self.city == 'Warsaw':
            options = {
                "1": "Contact the control tower and wait for instructions",
                "2": "Increase engine power",
                "3": "Check the landing gear"
            }
            current_answer = ["Contact the control tower and wait for instructions", "Increase engine power"]

            user_choice = input(
                "We are approaching the city of Warsaw. Suddenly, the control tower informs us of a problem with "
                "the landing gear. We have to make a decision.\n1. Contact the control tower and wait for instructions\n2. Increase engine power\n3. Check the landing gear\n")

            if user_choice in current_answer:
                print("We landed successfully at the alternate airport in Modlin.")
                print("We were close to the catastrophe, but the important thing is that we are all safe.")
                print("-" * 100)
                continue_execution = False
            elif user_choice in options.values():
                error_count += 1
                if error_count >= 3:
                    print("Wrong answer!!!")
                    print("Let's try again")
                    print('*' * 100)
                    continue_execution = False
                else:
                    print("Error! But you have more attempts ({}/3)".format(3 - error_count))
            else:
                print("Incorrect selection option!!!")
                print("Let's try again")
                print('*' * 100)

        continue_execution = True

        # Direction - Baghdad
        while continue_execution and self.city == 'Baghdad':
            options = {
                "1": "Contact the control tower and inform about the situation",
                "2": "Make an emergency landing",
                "3": "Use an aircraft fire extinguishing system"
            }
            current_answer = ["Contact the control tower and inform about the situation",
                              "Make an emergency landing"]

            user_choice = input(
                "There is a fire on board. The extinguishing system does not cope, we have to decide quickly. "
                "What should we do?\n1. Contact the control tower and inform about the situation\n2. Make an emergency landing\n3. Use an aircraft fire extinguishing system\n")

            if user_choice in current_answer:
                print("You made the right decision, we landed successfully at Baghdad Airport.")
                print("Fire services immediately dealt with the fire.")
                print("We have completed the first stage of our flight.")
                print("-" * 100)
                continue_execution = False
            elif user_choice in options.values():
                error_count += 1
                if error_count >= 3:
                    print("Wrong answer!!!")
                    print("Let's try again")
                    print('*' * 100)
                    continue_execution = False
                else:
                    print("Error! But you have more attempts ({}/3)".format(3 - error_count))
            else:
                print("Incorrect selection option!!!")
                print("Let's try again")
                print('*' * 100)

        if continue_execution:
            print("Error: The specified city is not in the list of available directions.")
            print("Please check your input or contact support for assistance.")

        return not continue_execution



if __name__ == "__main__":
    scenario = Scenario(True, True, True, True, True, True, True, True, True, True, True)
    scenario.RunScenario()