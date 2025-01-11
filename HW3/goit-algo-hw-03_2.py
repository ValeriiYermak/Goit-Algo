"""
Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови, що користувач
повинен мати можливість вказати рівень рекурсії.

"""
import turtle
import tkinter as tk

def draw_snowflake(level):
    """
    Draw a full Koch snowflake with the given recursion level.

    :param level: Recursion depth for the snowflake
    """
    print(f"Starting to draw Koch Snowflake at level {level}. Please wait...")

    # Налаштування екрану Turtle
    root = tk.Tk()
    root.title("Koch Snowflake")
    root.attributes('-topmost', True)  # Встановлення вікна поверх усіх інших
    root.update()  # Оновлює властивості вікна

    canvas = tk.Canvas(root, width=800, height=800)
    canvas.pack()

    # Інтеграція Turtle з Tkinter
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("#E2EA7C")
    t = turtle.RawTurtle(screen)
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Малювання сніжинки
    for _ in range(3):
        koch_snowflake(t, 400, level)
        t.right(120)

    print("Finished drawing. Close the window to exit.")
    root.mainloop()


def koch_snowflake(t, length, level):
    """
    Recursive function to draw a Koch snowflake segment.

    :param t: Turtle object
    :param length: Length of the segment
    :param level: Recursion depth
    """
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)
        t.right(120)
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)


if __name__ == "__main__":
    try:
        level = int(input("Enter the recursion level (e.g.2, 3 or more): "))
        if level < 0:
            print("Level must be a non-negative integer.")
        else:
            draw_snowflake(level)
    except ValueError as e:
        print(f"Invalid input: {e}")


