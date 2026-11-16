
from patient import Patient
from procedure import Procedure


def create_patient():
    print("Enter patient information:")

    first_name = input("First Name: ")
    middle_name = input("Middle Name: ")
    last_name = input("Last Name: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("ZIP: ")
    phone = input("Phone: ")
    emergency_contact = input("Emergency Contact: ")
    emergency_phone = input("Emergency Phone: ")

    return Patient(first_name, middle_name, last_name,
                   address, city, state, zip_code, phone,
                   emergency_contact, emergency_phone)


def create_procedure():
    print("\nEnter procedure information:")

    description = input("Description: ")
    date = input("Date: ")
    practitioner = input("Practitioner: ")

    while True:
        try:
            charge = float(input("Enter the charge: "))

            if charge > 0:
                break
            else:
                print("Please enter a positive number for charge.")

        except ValueError:
            print("Please enter a valid number for charge.")

    return Procedure(description, date, practitioner, charge)


def main():
    patient = create_patient()

    procedures = []

    print("\nAdd one or more procedures (enter 'n' to stop).")

    while True:
        again = input("Add a procedure? (y/n): ").strip().lower()

        if again == "n":
            break
        elif again == "y":
            procedures.append(create_procedure())
        else:
            print("Please enter y or n.")

    print("\nPatient and Procedure Information:")
    print(patient)
    print()

    total = 0.0

    for procedure in procedures:
        print(procedure)
        print()
        total += procedure.get_charge()

    print(f"Total Charges: {total:.2f}")


if __name__ == "__main__":
    main()
