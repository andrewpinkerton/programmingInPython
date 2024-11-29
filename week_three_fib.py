import turtle as tg


def main():
     # Can change colors
    colors: list = ['red', 'white', 'yellow', 'green', 'blue', 'darkblue', 'purple']
    line_color: str = 'brown'

    t: tg.Turtle = tg.Turtle()
    s: tg.Screen = tg.Screen()

    s.bgcolor('black')
    t.color(line_color)
    t.speed(0)
    t.width(2)

    # Fib Sequence
    for spot in range(1, 17):
        a: int = 0
        b: int = 1
        for _ in range(spot):
            c: int = a + b
            a = b
            b = c

        t.color(line_color, colors[spot % len(colors)])

        # Assignment Part
        t.begin_fill()
        for side in range(6):
            t.forward(a)
            t.right(90)
            if side == 4:
                t.end_fill()
        t.left(90)

    s.mainloop()


main()