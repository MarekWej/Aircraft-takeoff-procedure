# user_choice = input(
#                 "Passengers started shouting that there were terrorists on the plane, what should we do?\n1. "
#                 "Lock the cockpit door and continue flying, to the designated destination\n2. "
#                 "Neutralize the terrorists at all costs\n3. Negotiate with terrorists\n Select the option: "
#             ).strip().lower()
#
#
# def Directions(self):
#     continue_execution = True
#     error_count = 0
#
#     # Direction - Tokyo
#     while continue_execution:
#         if self.city == 'Tokyo':
#             options = {
#                 "1": "Notify the flight control station",
#                 "2": "Notify passengers of the problem",
#                 "3": "Create a panic"
#             }
#
#             current_answer = ["Notify the flight control station", "Notify passengers of the problem"]
#             user_choice = input(
#                 "It seems that something is wrong with engine #1, its power has dropped. We are almost there, "
#                 "above the city. What should we do?\n1. Notify the flight control station"
#                 "\n2. Notify passengers of the problem\n3. Increase the power of engine #2\n"
#                 "Select the option: ").strip().lower()
#
#             if user_choice == "1 2" or user_choice == "2 1":
#                 print(
#                     "Yes, sir. I am notifying the flight control station and passengers of the problem that has arisen.")
#                 print('-' * 100)
#                 continue_execution = False
#
#             elif user_choice in options:
#                 if options[user_choice] in current_answer:
#                     print('-' * 100)
#                     print("Executes:", options[user_choice], "but we need to do something else.")
#                     error_count += 1
#                     print('-' * 100)
#                     print("Wrong answers = {}/3".format(error_count))
#                     print('-' * 100)
#                     print("Let's try again.")
#                     print('-' * 100)
#                 else:
#                     error_count += 1
#                     print("Wrong answers = {}/3".format(error_count))
#                     print('-' * 100)
#
#                     if error_count >= 3:
#                         print("You have exceeded the maximum number of incorrect answers. Exiting.")
#                         print("Wrong answers = {}/3".format(error_count))
#                         return
#                     print("Let's try again.")
#                     time.sleep(2)
#             else:
#                 error_count += 1
#                 print('-' * 100)
#                 print("Wrong answers = {}/3".format(error_count))
#                 print('-' * 100)
#                 if error_count >= 3:
#                     print("You have exceeded the maximum number of incorrect answers. Exiting.")
#                     print("Wrong answers = {}/3".format(error_count))
#                     return
#                 print("Incorrect selection option!!!")
#                 print("Let's try again.")
#                 time.sleep(2)
#
#         # Direction - Warsaw
#         elif self.city == "Warsaw":
#             options = {
#                 "1": "Lock the cockpit door and continue flying to the designated destination",
#                 "2": "Neutralize the terrorists at all costs",
#                 "3": "Negotiate with terrorists"
#             }
#             current_answer = "Lock the cockpit door and continue flying to the designated destination"
#             user_choice = input(
#                 "Passengers started shouting that there were terrorists on the plane. What should we do?\n1. "
#                 "Lock the cockpit door and continue flying to the designated destination\n2. "
#                 "Neutralize the terrorists at all costs\n3. Negotiate with terrorists\nSelect the option: ").strip()
#
#             if user_choice in options:
#                 if options[user_choice] == current_answer:
#                     print("That's right, pilot! Close the door immediately!!!")
#                     print('-' * 100)
#                     break
#                 else:
#                     error_count += 1
#                     print('-' * 100)
#                     print("Wrong answers = {}/3".format(error_count))
#                     print('-' * 100)
#                     if error_count >= 3:
#                         print("You have exceeded the maximum number of incorrect answers. Exiting.")
#                         return
#                     print("Let's try again.")
#                     print('-' * 100)
#             else:
#                 error_count += 1
#                 print('-' * 100)
#                 print("Wrong answers = {}/3".format(error_count))
#                 print('-' * 100)
#                 if error_count >= 3:
#                     print("You have exceeded the maximum number of incorrect answers. Exiting.")
#                     print("Wrong answers = {}/3".format(error_count))
#                     return
#                 print("Incorrect selection option!!!")
#                 print("Let's try again.")
#                 print('-' * 100)
#         else:
#             error_count += 1
#             if error_count >= 3:
#                 print("You have exceeded the maximum number of incorrect answers. Exiting.")
#                 print("Wrong answers = {}/3".format(error_count))
#                 return
#             print("Incorrect selection option!!!")
#             print("Let's try again.")
#
#         # Direction - Sydney
#         elif self.city == 'Sydney':
#         options = {
#             "1": "Perform a routine landing",
#             "2": "Initiate emergency landing procedures",
#             "3": "Request assistance from air traffic control"
#         }
#         current_answer = "Perform a routine landing"
#         user_choice = input(
#             "The weather conditions have worsened unexpectedly. What should we do?\n1. Perform a routine landing"
#             "\n2. Initiate emergency landing procedures\n3. Request assistance from air traffic control"
#             "\nSelect the option: ").strip()
#
#         if user_choice in options:
#             if options[user_choice] == current_answer:
#                 print("You made the correct decision. Prepare for landing!")
#                 print('-' * 100)
#                 break
#             else:
#                 error_count += 1
#                 print('-' * 100)
#                 print("Wrong answers = {}/3".format(error_count))
#                 print('-' * 100)
#                 if error_count >= 3:
#                     print("You have exceeded the maximum number of incorrect answers. Exiting.")
#                     return
#                 print("Let's try again.")
#                 print('-' * 100)
#         else:
#             error_count += 1
#             print('-' * 100)
#             print("Wrong answers = {}/3".format(error_count))
#             print('-' * 100)
#             if error_count >= 3:
#                 print("You have exceeded the maximum number of incorrect answers. Exiting.")
#                 print("Wrong answers = {}/3".format(error_count))
#                 return
#             print("Incorrect selection option!!!")
#             print("Let's try again.")
#             print('-' * 100)
#
#     else:
#         error_count += 1
#         if error_count >= 3:
#             print("You have exceeded the maximum number of incorrect answers. Exiting.")
#             print("Wrong answers = {}/3".format(error_count))
#             return
#         print("Incorrect selection option!!!")
#         print("Let's try again.")


# "The computer has calculated that the altitude is sufficient to reach the nearest airport in "
#                          "an emergency, but the pilot's calculations show that we will not reach it and will collide "
#                          "with buildings