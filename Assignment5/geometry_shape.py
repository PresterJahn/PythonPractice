import turtle

def main():
    choice = ""

    while choice != "4":
        print("Shape Menu")
        print("1) Draw a Square")
        print("2) Draw a Circle")
        print("3) Draw an Equilateral Triangle")
        print("4) Quit")

        choice = input("Enter your choice: ")

        while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            choice = input("Enter your choice: ")

        if choice == "1":
            x = int(input("Enter the starting X coordinate: "))
            y = int(input("Enter the starting Y coordinate: "))
            side = int(input("Enter the length of a side: "))
            color = input("Enter the fill color: ")

            draw_square(x, y, side, color)

        elif choice == "2":
            x = int(input("Enter the X coordinate of the center: "))
            y = int(input("Enter the Y coordinate of the center: "))
            radius = int(input("Enter the radius: "))
            color = input("Enter the fill color: ")

            draw_circle(x, y, radius, color)

        elif choice == "3":
            x = int(input("Enter the starting X coordinate: "))
            y = int(input("Enter the starting Y coordinate: "))
            side = int(input("Enter the length of a side: "))
            color = input("Enter the fill color: ")

            draw_triangle(x, y, side, color)

        elif choice == "4":
            print("Exiting the program.")

def draw_square(x, y, side, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.fillcolor(color)
    turtle.begin_fill()

    for i in range(4):
        turtle.forward(side)
        turtle.right(90)

    turtle.end_fill()

def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()

    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_triangle(x, y, side, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.fillcolor(color)
    turtle.begin_fill()

    for i in range(3):
        turtle.forward(side)
        turtle.left(120)

    turtle.end_fill()


if __name__ == "__main__":
    main()