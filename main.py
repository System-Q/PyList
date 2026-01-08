import os

lists_path = "lists"
pre_prompt = "\nMake a selection, or type ':q' to go back or exit"
prompt = ">>>> "


def heading(top_text: str, bottom_text: str):
    divider = "-" * 40

    top_char_count = 0
    for chars in top_text:
        top_char_count += 1

    bottom_char_count = 0
    for chars in bottom_text:
        bottom_char_count += 1

    # determine how many dashes to add to the string to make it the correct length
    to_add_top = 40 - top_char_count
    to_add_bottom = 40 - bottom_char_count

    # split the value so that the correct ammount gets added to each side
    to_add_top = to_add_top // 2
    to_add_bottom = to_add_bottom // 2

    new_top_text = "-" * to_add_top + top_text + "-" * to_add_top
    new_bottom_text = "-" * to_add_bottom + bottom_text + "-" * to_add_bottom

    os.system("clear")
    print(f"{divider}\n")
    print(f"{new_top_text}")
    print(f"{new_bottom_text}\n")
    print(f"{divider}\n")


def new_list():
    while True:
        heading("Create a new list", "Give your list a name")

        invalid_ins = [
            "",
            " ",
        ]

        print(pre_prompt)
        list_name = input(prompt)

        if list_name == ":q":
            welcome_screen()

        while list_name in invalid_ins:
            print("Field cannot be blank.")
            list_name = input(prompt)

        with open(f"{lists_path}/{list_name}", "a") as new_list:
            while True:
                print("Add an item to the list, or type 'q' to exit to main menu")

                usr_item = input(prompt)
                if usr_item == ":q":
                    break

                else:
                    new_list.write(f"{usr_item}\n")


def view_lists():
    while True:
        heading("View a List", "Select a list to view")

        usr_lists = os.listdir(lists_path)
        file_count = 0

        for files in usr_lists:
            file_count += 1
            print(f"{file_count}: {files}")

        print(pre_prompt)
        usr_choice = input(prompt)

        if usr_choice == ":q":
            welcome_screen()

        while usr_choice not in usr_lists:
            print("Invalid option. Please enter a valid file name")
            usr_choice = input(prompt)

        while usr_choice in usr_lists:
            with open(f"{lists_path}/{usr_choice}", "r") as listicle:
                listicle = listicle.read()
                print("\n" + listicle)

            print(f"View another list? {pre_prompt}")
            usr_choice = input(prompt)
            if usr_choice == ":q":
                break


def delete_list():
    while True:
        heading("Delete a List", "Select a list to delete")

        usr_lists = os.listdir(lists_path)
        file_count = 0

        for files in usr_lists:
            file_count += 1
            print(f"{file_count}: {files}")

        print(pre_prompt)
        usr_choice = input(prompt)

        if usr_choice == ":q":
            welcome_screen()

        while usr_choice not in usr_lists:
            print("Invalid option. Please enter a valid file name")
            usr_choice = input(prompt)

        while usr_choice in usr_lists:
            os.system(f"rm {lists_path}/{usr_choice}")

            print(f"Delete another list? {pre_prompt}")
            usr_choice = input(prompt)
            if usr_choice == ":q":
                break


def welcome_screen():
    heading("Welcome to PyList", "Written by System-Q")

    usr_options = {
        "1": "Create a new list",
        "2": "View a list",
        "3": "Edit a list",
        "4": "Delete a list",
    }

    print("Main Menu\n")
    for key, value in usr_options.items():
        print(f"{key}: {value}")

    print(pre_prompt)
    usr_choice = input(prompt)
    print(usr_choice)

    if usr_choice == ":q":
        quit()

    while usr_choice not in usr_options.keys():
        print("Invalid option. Please select a valid option")
        usr_choice = input(prompt)

    if int(usr_choice) == 1:
        new_list()

    if int(usr_choice) == 2:
        view_lists()

    if int(usr_choice) == 4:
        delete_list()

    if usr_choice == ":q":
        quit()


welcome_screen()
