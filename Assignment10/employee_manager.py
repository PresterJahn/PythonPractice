
import pickle
from employee import Employee

FILENAME = "employees.dat"


def load_employees():
    try:
        with open(FILENAME, "rb") as file:
            employees = pickle.load(file)
    except (FileNotFoundError, EOFError):
        employees = {}

    return employees


def save_employees(employees):
    with open(FILENAME, "wb") as file:
        pickle.dump(employees, file)


def display_menu():
    print("\nMenu")
    print("---------------------------------------")
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Change an existing employee")
    print("4. Delete an employee")
    print("5. Quit the program")


def look_up_employee(employees):
    id_number = input("Enter an employee ID number: ")

    if id_number in employees:
        print(employees[id_number])
    else:
        print("The specified ID number was not found")


def add_employee(employees):
    name = input("Enter employee name: ")
    id_number = input("Enter employee ID number: ")
    department = input("Enter employee department: ")
    title = input("Enter employee title: ")

    if id_number not in employees:
        employees[id_number] = Employee(
            name, id_number, department, title
        )
        print("The new employee has been added.")
    else:
        print("An employee with that ID already exists.")


def change_employee(employees):
    id_number = input("Enter employee ID number: ")

    if id_number in employees:
        name = input("Enter the new name: ")
        department = input("Enter the new department: ")
        title = input("Enter the new title: ")

        employees[id_number].set_name(name)
        employees[id_number].set_department(department)
        employees[id_number].set_title(title)

        print("Employee information updated.")
    else:
        print("The specified ID number was not found")


def delete_employee(employees):
    id_number = input("Enter employee ID number: ")

    if id_number in employees:
        del employees[id_number]
        print("Employee information deleted.")
    else:
        print("The specified ID number was not found")


def main():
    employees = load_employees()

    choice = 0

    while choice != 5:
        display_menu()

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            look_up_employee(employees)

        elif choice == 2:
            add_employee(employees)
            save_employees(employees)

        elif choice == 3:
            change_employee(employees)
            save_employees(employees)

        elif choice == 4:
            delete_employee(employees)
            save_employees(employees)

        elif choice == 5:
            save_employees(employees)

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
