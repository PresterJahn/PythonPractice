
import os
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Location of the email data file
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, 'email.dat')


def main():
    emails = load_emails()
    choice = get_user_choice()

    while choice != QUIT:
        if choice == LOOK_UP:
            look_up(emails)
        elif choice == ADD:
            add(emails)
            save_emails(emails)
        elif choice == CHANGE:
            change(emails)
            save_emails(emails)
        elif choice == DELETE:
            delete(emails)
            save_emails(emails)

        choice = get_user_choice()


def load_emails():
    try:
        input_file = open(FILENAME, 'rb')
        emails = pickle.load(input_file)
        input_file.close()
    except (FileNotFoundError, EOFError):
        emails = {}

    return emails


def get_user_choice():
    print('\nMenu')
    print('-' * 43)
    print('1. Look up an email address')
    print('2. Add a new name and email address')
    print('3. Change an existing email address')
    print('4. Delete a name and email address')
    print('5. Quit the program')

    choice = input('\nEnter your choice: ')

    while choice not in ('1', '2', '3', '4', '5'):
        print('Please enter a number from 1 to 5.')
        choice = input('Enter your choice: ')

    return int(choice)


def look_up(emails):
    name = input('Enter a name: ')

    if name in emails:
        print('  Name:', name)
        print('Email:', emails[name])
    else:
        print('The specified name was not found.')


def add(emails):
    name = input('Enter name: ')

    if name not in emails:
        address = input('Enter email address: ')
        emails[name] = address
        print('Name and address have been added.')
    else:
        print('That name already exists.')


def change(emails):
    name = input('Enter name: ')

    if name in emails:
        address = input('Enter the new address: ')
        emails[name] = address
        print('Information updated.')
    else:
        print('The specified name was not found.')


def delete(emails):
    name = input('Enter name: ')

    if name in emails:
        del emails[name]
        print('Information deleted.')
    else:
        print('The specified name was not found.')


def save_emails(emails):
    output_file = open(FILENAME, 'wb')
    pickle.dump(emails, output_file)
    output_file.close()


if __name__ == '__main__':
    main()
