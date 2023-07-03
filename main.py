import random
import socket
import string
import calendar
from ctypes import windll

def set_window_always_on_top():
    HWND_TOPMOST = -1
    HWND = windll.user32.GetForegroundWindow()
    windll.user32.SetWindowPos(HWND, HWND_TOPMOST, 0, 0, 0, 0, 0x0001)

def convert_month_number(month_number):
    return calendar.month_abbr[month_number]

def generate_name():
    prefixes = ["Ava", "Eli", "Emma", "Liam", "Olivia", "Noah", "Isabella", "Sophia", "Mia", "Charlotte"]
    suffixes = ["n", "lia", "n", "am", "h", "n", "a", "h", "a", "e"]

    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)

    return prefix + suffix


def generate_date():
    day = random.randint(1, 31)
    month = random.randint(1, 12)
    year = 2000

    return f"{day:02d}/{convert_month_number(month)}/{year}"


def generate_display_name():
    first_name = generate_name()
    last_name = generate_name()
    numbers = random.randint(1000, 9999)

    display_name = first_name + last_name + str(numbers)
    first_last_name = first_name + " " + last_name

    return display_name, first_last_name


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_epic_games_code(email):
    # Generate a random display name, its corresponding first and last name, and a date
    display_name, first_last_name = generate_display_name()
    date = generate_date()

    # Get the computer's IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    # Generate a random password with a length of 10 characters
    password = generate_password(10)

    # Save the account details to a text file
    with open("../python non virus/account_details.txt", "a") as file:
        file.write("Email: " + email + "\n")
        file.write("Display Name: " + display_name + "\n")
        file.write("First and Last Name: " + first_last_name + "\n")
        file.write("Date: " + date + "\n")
        file.write("Password: " + password + "\n")
        file.write("-------------------------------\n")

    # Print the generated details
    print("-------------------------")
    print("Email:", email)
    print("Generated Display Name:", display_name)
    print("Generated First and Last Name:", first_last_name)
    print("Generated Date:", date)
    print("Generated Password:", password)
    print("-------------------------")

def main():
    set_window_always_on_top()

    print(
        "               _                            _                _ _                                                _             ")
    print(
        "              | |                          | |              (_) |                                              | |            ")
    print(
        " __      _____| | ___ ___  _ __ ___   ___  | |_ ___    _ __  _| |_ __ _ _   _    __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ ")
    print(
        " \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | '_ \| | __/ _` | | | |  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|")
    print(
        "  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | | | | | || (_| | |_| | | (_| |  __/ | | |  __/ | | (_| | || (_) | |   ")
    print(
        "   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_| |_|_|\__\__,_|\__, |  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   ")
    print(
        "                                                                         __/ |   __/ |                                        ")
    print(
        "                                                                        |___/   |___/                                         ")

    while True:
        print("Please select an option:")
        print("1. Epic Games")
        print("2. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Click here to generate your temporary email for your epic account: 'https://temp-mail.org/'")
            email = input("Enter your temporary generated email address: ")
            generate_epic_games_code(email)
            generate_more = input("Do you want to generate more accounts? (Y/N): ")
            if generate_more.upper() == "N":
                break
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

    input("Press Enter to exit...")

# Execute the main function
if __name__ == "__main__":
    main()
