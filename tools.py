def LaunchSequence_info(self):
    root = Tk()
    root.title("Launch Sequence Info")
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