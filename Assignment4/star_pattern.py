# Outer loop controls the rows
for row in range(7, 0, -1):

    # Inner loop controls the columns
    for column in range(row):
        print("*", end="")

    # Move to the next line
    print()