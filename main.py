import random
import sys
from datetime import datetime

MONTH = datetime.now()
MONTH_STRING = MONTH.strftime("%B").upper()

def main():
    display_header()
    display_ineligible_names()
    print()
    while True:
        cmd = input(
            f"Choosing a teacher for {MONTH_STRING}, Enter to choose or [q] to quit\nor perform a full [RESET]: ")
        clean_cmd = cmd.strip().lower()
        if clean_cmd == '':
            teacher_spotlight = open_eligible_names_and_retrieve_name()
            display_name_choice(teacher_spotlight)
            remove_selected_name(teacher_spotlight)
            write_chosen_name_to_ineligible_names(teacher_spotlight)
        elif clean_cmd == 'q':
            print("\nGOODBYE!")
            sys.exit()
        elif clean_cmd == 'reset':
            print("Are you sure you want to reset? (y/n): ")
            r = input().lower().strip()
            if r == 'y':
                perform_data_reset()
            else:
                continue


def display_header():
    print("*** TEACHER SPOTLIGHT SELECTION TOOL ***\n")


def open_eligible_names_and_retrieve_name(file='eligible_names.txt'):
    try:
        with open(file, 'r') as f:
            names = f.readlines()
    except FileNotFoundError:
        print("Eligible names not found!")
    else:
        return random.choice(names)


def remove_selected_name(name_to_remove, file='eligible_names.txt'):
    try:
        with open(file, 'r') as f:
            names = f.readlines()
    except FileNotFoundError:
        print("Eligible names file not found.")

    try:
        with open(file, 'w') as f:
            for name in names:
                if name.strip().lower() != name_to_remove.strip().lower():
                    f.write(name)
    except FileNotFoundError:
        print("Eligible names file not found.")
    else:
        print(f"Eligible names updated, {name_to_remove.upper().strip()} removed!\n")


def display_name_choice(name):
    print(f"*** TEACHER SPOTLIGHT CHOICE - {MONTH_STRING} ***\n")
    print(f'\t\t{name.upper()}')
    print()


def display_ineligible_names(file='ineligible_names.txt'):
    try:
        with open(file, 'r') as f:
            names = f.readlines()
    except FileNotFoundError:
        print("Ineligible names not found!")
    else:
        print("Previously chosen teachers: ")
        for name in names:
            print(name)


def write_chosen_name_to_ineligible_names(name, file='ineligible_names.txt'):
    try:
        with open(file, 'a') as f:
            f.write(name)
    except FileNotFoundError:
        print("Ineligible names file not found.")
    else:
        print(f"Ineligible names updated, {name.upper().strip()} added!\n")


def populate_eligible_names(names, file='eligible_names.txt'):
    with open(file, 'w') as f:
        for name in names:
            f.write(name)


def perform_data_reset(inel_file='ineligible_names.txt', perm='perm_names.txt'):
    try:
        with open(inel_file, 'w') as f:
            f.write('')
    except FileNotFoundError:
        print("Ineligible names file not found.")
    else:
        print("\n**RESET STARTING**\n")
        print("Ineligible names set to empty.")

    try:
        with open(perm, 'r') as perm_file:
            all_names = perm_file.readlines()
    except FileNotFoundError:
        print("Permanent names file not found.")
    else:
        print("Reading names from permanent name data source.")

    try:
        populate_eligible_names(all_names)
    except FileNotFoundError:
        print("An error occurred while opening eligible_names")
    except:
        print("An error occurred while transferring from permanent names to eligible names.")
    else:
        print("\n*** RESET COMPLETE ***\n")
        print("Eligible names has been successfully reset to the original faculty roster.\n")


if __name__ == '__main__':
    main()
