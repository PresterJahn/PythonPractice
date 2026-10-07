from pathlib import Path

MIN_CELSIUS = 0
MAX_CELSIUS = 50


# find the file in the same folder that hosts the Python script
TEMPERATURE_FILE = Path(__file__).resolve().parent / "temperature_forloop.txt"


def main():
    celsius = get_celsius()

    # this section is to test both for-loop and while-loop
    # for searching target in a file

    fahrenheit_forloop = find_match_forloop(celsius)
    fahrenheit_whileloop = find_match_whileloop(celsius)

    print(f"For-loop search result: {fahrenheit_forloop}")
    print(f"While-loop search result: {fahrenheit_whileloop}")

    if fahrenheit_forloop is not None:
        print(
            f"Match found: {celsius} Celsius is "
            f"{fahrenheit_forloop:.2f} Fahrenheit."
        )

    else:
        fahrenheit = (celsius * 1.8) + 32

        append_record(celsius, fahrenheit)

        print(
            f"No match found. New record added: "
            f"{celsius} Celsius = {fahrenheit:.2f} Fahrenheit."
        )


def get_celsius():
    # enforce the user to enter a good celsius
    # temperature between 0-50

    celsius = int(input("Enter a celsius degree (0-50): "))

    while celsius < MIN_CELSIUS or celsius > MAX_CELSIUS:
        print(
            f"Invalid input. Please enter a temperature between "
            f"{MIN_CELSIUS} and {MAX_CELSIUS}."
        )

        celsius = int(input("Enter a celsius degree (0-50): "))

    return celsius


def find_match_forloop(celsius):
    fahrenheit = None

    with open(TEMPERATURE_FILE, "r") as infile:
        skip_header(infile)

        for line in infile:
            degree_text, fahrenheit_text = line.split("\t\t")

            if int(degree_text) == celsius:
                fahrenheit = float(fahrenheit_text)

    return fahrenheit


def find_match_whileloop(celsius):
    fahrenheit = None

    with open(TEMPERATURE_FILE, "r") as infile:
        skip_header(infile)

        line = infile.readline()

        while line != "":
            degree_text, fahrenheit_text = line.split("\t\t")

            if int(degree_text) == celsius:
                fahrenheit = float(fahrenheit_text)

            line = infile.readline()

    return fahrenheit


# this function removes the header and dash line
def skip_header(infile):
    infile.readline()  # skip the header line
    infile.readline()  # skip the dashed separator line


def append_record(celsius, fahrenheit):
    # append a new record to the existing file

    with open(TEMPERATURE_FILE, "a") as outfile:
        outfile.write(f"{celsius:>8}\t\t{fahrenheit:>8.2f}\n")


if __name__ == "__main__":
    main()