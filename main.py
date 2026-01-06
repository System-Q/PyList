import os

lists_path = "lists"
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
    heading("Create a new list", "Give your list a name")


def view_lists():
    heading("View a List", "Select a list to view")

    usr_lists = os.listdir(lists_path)
    file_count = 0

    for files in usr_lists:
        file_count += 1
        print(f"{file_count} {files}")

    print(f"{file_count + 1} Main Menu\n")

    usr_choice = input(prompt)
    if usr_choice in usr_lists:
        with open(f"{lists_path}/{usr_choice}", "r") as listicle:
            listicle = listicle.read()
            print(listicle)

    elif int(usr_choice) == file_count + 1:
        welcome_screen()

    else:
        print("Error, file not found")
        return


def welcome_screen():
    heading("Welcome to PyList", "Bottom Text")

    print("Please make a selection:\n")
    print("1: Create a new list")
    print("2: Edit a list")
    print("3: View a list")
    print("4: Delete a list\n")

    usr_choice = input(prompt)
    print(usr_choice)

    if int(usr_choice) == 3:
        view_lists()


welcome_screen()
