import re
from turtle import Turtle, Screen
from calendar import month_name

import requests as rq


def main():
    url = "https://en.wikipedia.org/wiki/Terraria"

    response: rq.Response = rq.get(url)
    page_content: str = response.text

    months: dict = count_months(page_content)

    s = Screen()
    s.title("Turtle Color Months")
    s.colormode(255)
    s.bgcolor("black")

    draw_the_bars(months)

    s.mainloop()


def draw_the_bars(months: dict) -> None:
    """Draw a bargraph using turtle graphics."""

    x = -300
    y = -200
    r = 255
    g = 0
    b = 255

    for key, value in months.items():
        month_letter: str = key[0]
        distance: int = value * 5
        draw_bar(month_letter, distance, x, y, r, g, b)
        
        x += 45
        g += 21
        r -= 21


def draw_bar(
        letter: str,
        distance: int,
        x: int,
        y: int,
        r: int,
        g: int,
        b: int,
) -> None:
    """Draw a bar for the given month."""
    
    font = ("Consolas", 20, "bold")

    t = Turtle()
    t.hideturtle()
    t.color((r, g, b))
    t.teleport(x, y)
    t.write(letter, font=font)
    t.left(90)
    t.teleport(x, y+50)
    t.pensize(40)
    t.forward(distance)


def count_months(page_content: str) -> dict:
    """Count the number of times each month "appears" """

    months = {}

    for i in range(1, 13):
        month = month_name[i]

        pattern: str = month
        
        occurred = rf"\b{pattern}\b"

        amount = len(re.findall(occurred, page_content))

        months[month] = amount

    return months


if __name__ == "__main__":
    main()