if self.city == 'Tokyo':

    question_label_Tokyo = Label(info_frame, text="It seems that something is wrong with engine #1, "
                                                  "its power has dropped. We are almost there,"
                                                  "above the city. What should we do?")
    question_label_Tokyo.pack()

    options = {
        "1": "Notify the flight control station",
        "2": "Notify passengers of the problem",
        "3": "Create a panic"
    }

    current_answer = ["Notify the flight control station", "Notify passengers of the problem"]

    var1 = BooleanVar()
    options1 = Checkbutton(info_frame, text=options["1"], variable=var1)
    options1.pack()

    var2 = BooleanVar()
    options2 = Checkbutton(info_frame, text=options["2"], variable=var2)
    options2.pack()

    var3 = BooleanVar()
    options1 = Checkbutton(info_frame, text=options["3"], variable=var3)
    options1.pack()


    def submit_info_Tokyo():
        choice = []

        if var1.get():
            choice.append(options["1"])
        if var2.get():
            choice.append(options["2"])
        if var3.get():
            choice.append(options["3"])

        if sorted(choice) == sorted(current_answer):
            print(
                "Yes, sir. I am notifying the flight control station and passengers of the problem that has arisen.")
            print('-' * 100)
            root.destroy()

        else:
            nonlocal error_count
            error_count += 1
            print('-' * 100)
            print("Wrong answers = {}/{}".format(error_count, max_attempts))
            print('-' * 100)
            if error_count >= max_attempts:
                print("You have exceeded the maximum number of incorrect answers. Exiting.")
                root.destroy()
            print("Let's try again.")
            print('-' * 100)


    submit_button = Button(info_frame, text="Submit", command=submit_info_Tokyo)
    submit_button.pack()
    root.mainloop()


