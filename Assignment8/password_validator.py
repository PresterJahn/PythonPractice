
def check_password(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False

    if not password.isalnum():
        print("Password can only contain letters and digits.")
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if not (has_upper and has_lower and has_digit):
        print("Password must contain at least one uppercase letter, one lowercase letter, and one digit.")
        return False

    return True


def main():
    password = input("Enter a password: ")

    if check_password(password):
        print("Password is valid.")
    else:
        print("Password is invalid.")


if __name__ == "__main__":
    main()
