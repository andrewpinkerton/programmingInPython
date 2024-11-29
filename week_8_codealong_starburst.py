from turtle import Turtle, Screen


def main():
    colors = [
        (0, 0, 255),
        (0, 36, 255),
        (0, 73, 255),
        (0, 109, 255),
        (0, 146, 255),
        (0, 182, 255),
        (0, 219, 255),
    ]
    symbols = [
        "\u2745",
        "\u2746",
        "\u2747",
        "\u2748",
        "\u2749",
        "\u274A",
        "\u274B",
    ]

    t = Turtle()
    s = Screen()

    s.colormode(255)
    s.bgcolor("black")
    s.title("Turtle Starburst")
    t.speed(0)
    t.penup()

    draw_shapes(t, colors, symbols)

    s.mainloop()


def draw_shapes(
        t: Turtle,
        colors: tuple,
        symbols: tuple,
) -> None:
    """Draws starburst shape using for loop"""
    for star in range(2, 360):
        color: tuple = colors[star % len(colors)]
        symbol: str = symbols[star % len(symbols)]
        font_size: int = star // 2
        font: tuple = ("Consolas", font_size, "normal")

        t.pencolor(color)
        t.forward(star * 2)
        t.write(symbol, font=font)
        t.right(49)

if __name__ == "__main__":
    main()