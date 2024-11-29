import turtle as tg
import random as rm


def main():
    t = tg.Turtle()
    s = tg.Screen()
     
    # Can change colors
    s.bgcolor('black')

    # Can change colors
    colors: list = ['red', 'white', 'blue', 'orange', 'purple', 'green', 'pink', 'yellow', 'brown']

    count: int = 0
    maximum: int = 1000

    while count < maximum:
        x: int = rm.randint(-500, 500)
        y: int = rm.randint(-500, 500)
        size: int = rm.randint(10, 75)

        t.teleport(x,y)

        # Assignment part
        if x < -167 and y < 167:
            t.dot(size, colors[0])
        elif x < 167 and y < 167:
            t.dot(size, colors[1])
        elif x > 167 and y < 167:
            t.dot(size, colors[2])

        if x < -167 and y > -167:
            t.dot(size, colors[3])
        elif x < 167 and y > -167:
            t.dot(size, colors[4])
        elif x > 167 and y > -167:
            t.dot(size, colors[5])

        if x < -167 and y > 167:
            t.dot(size, colors[6])
        elif x < 167 and y > 167:
            t.dot(size, colors[7])
        elif x > 167 and y > 167:
            t.dot(size, colors[8])

        count += 1

    s.mainloop()


main()