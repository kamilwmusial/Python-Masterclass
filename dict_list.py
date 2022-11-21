available_parts = {"1": ("computer"),
                   "2": ("monitor"),
                   "3": ("keyboard"),
                   "4": ("mouse"),
                   "5": ( "hdmi"),
                   "6": ("dvd drive"),
}

current_choice = None
computer_parts = []     # create empty list
del available_parts["6"]    # remove a part from the dictionary
available_parts["7"] = "mouse mat"  # add a part to the dictionary

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            # it is already in so remove it
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part)
        else:
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part)
        print(f"Your list now contains: {computer_parts}")
    else:
        print("Please choose from: ")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")

