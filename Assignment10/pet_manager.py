
from pet import Pet


def main():
    name = input("Enter the name of the pet: ")
    animal_type = input("Enter the type of animal: ")
    age = int(input("Enter the age of the pet: "))

    my_pet = Pet(name, animal_type, age)

    print("Here is the data that you entered:")
    print(my_pet)


if __name__ == "__main__":
    main()
