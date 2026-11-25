"""Generate passwords in the terminal using Python's secure secrets module."""

import secrets
import string


def ask_for_number(question, default, minimum, maximum):
    """Ask for a number and repeat until the answer is in the allowed range."""
    while True:
        answer = input(f"{question} [{default}]: ").strip()

        if answer == "":
            return default

        if answer.isdigit():
            number = int(answer)
            if minimum <= number <= maximum:
                return number

        print(f"Please enter a whole number from {minimum} to {maximum}.")


def ask_yes_no(question, default=True):
    """Ask a yes/no question. Enter keeps the default answer."""
    default_text = "Y/n" if default else "y/N"

    while True:
        answer = input(f"{question} ({default_text}): ").strip().lower()

        if answer == "":
            return default
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False

        print("Please answer with y or n.")


def generate_password(length, include_numbers, include_symbols):
    """Create one password with at least one character from each selected group."""
    character_groups = [string.ascii_lowercase, string.ascii_uppercase]

    if include_numbers:
        character_groups.append(string.digits)
    if include_symbols:
        character_groups.append(string.punctuation)

    # Start with one character from every selected group.
    password_characters = [secrets.choice(group) for group in character_groups]

    # Fill the remaining positions from all selected characters.
    all_characters = "".join(character_groups)
    remaining_length = length - len(password_characters)

    for _ in range(remaining_length):
        password_characters.append(secrets.choice(all_characters))

    # Mix the characters so the required characters are not always at the start.
    secrets.SystemRandom().shuffle(password_characters)
    return "".join(password_characters)


def main():
    print("\n=== Secure Password Generator ===\n")
    print("Choose your password settings. Press Enter to use the default.\n")

    length = ask_for_number("Password length (8-128)", 16, 8, 128)
    count = ask_for_number("How many passwords? (1-20)", 1, 1, 20)
    include_numbers = ask_yes_no("Include numbers?", default=True)
    include_symbols = ask_yes_no("Include symbols?", default=True)

    print("\nGenerated password(s):\n")
    for number in range(1, count + 1):
        password = generate_password(length, include_numbers, include_symbols)
        print(f"{number}. {password}")

    print("\nKeep your passwords private and store them in a trusted password manager.")


if __name__ == "__main__":
    main()
