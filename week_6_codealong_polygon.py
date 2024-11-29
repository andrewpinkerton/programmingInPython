from turtle import Turtle, Screen
from random import randint


def main():
    number_of_shapes = 20
    max_sides = 8

    t = Turtle()
    s = Screen()

    s.colormode(255)
    s.bgcolor("black")
    t.color("cyan")
    t.speed(0)

    generate_shapes(number_of_shapes, max_sides, t)
    s.mainloop()


def generate_shapes(
        number_of_shapes: int, 
        max_sides: int,
        t: Turtle,
) -> None:
    """Generates a random shape"""

    for shape in range(number_of_shapes):
        num_sides = randint(3, max_sides)

        angle: float = calculate_angle(num_sides)

        #Move to a function: random_pos(args?)
        pos: tuple = random_pos()

        #Move to a function: random_color(args?)
        color: tuple = random_color()

        side_length: int = 200 / num_sides

        # Move to a function: draw_shape
        draw_shape(num_sides, side_length, angle, t, pos, color)


def calculate_angle(num_sides: int) -> float:
    """Calculate an angle based on number of sides."""

    return 360 / num_sides


def random_pos() -> tuple:
    """Generates a random position"""

    pos: tuple = (randint(-300, 300), randint(-300, 300))

    return pos


def random_color() -> tuple:
    """Generates a random color"""

    r: int = randint(0, 255)
    g: int = randint(0, 255)
    b: int = randint(0, 255)
    color: tuple = (r, g, b)

    return color


def draw_shape( 
        num_sides: int,
        side_length: int, 
        angle: float, 
        t: Turtle, 
        pos: tuple, 
        color: tuple
) -> None:
    """Uses the turtle to draw the shape"""

    t.teleport(pos[0], pos[1])
    t.color(color)

    for side in range(num_sides):
        t.forward(side_length)
        t.right(angle)


if __name__ == "__main__":
    main()