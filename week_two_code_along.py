import turtle

# Setting up our pen and paper
t = turtle.Turtle()
t2 = turtle.Turtle()
s = turtle.Screen()

# Background Color and Speed
s.bgcolor('gray')
t.speed(0)
t2.speed(0)
s.colormode(255)

r = 120
g = 120
b = 120

count  = 0

while True:
    t.color(r, g, b)
    t2.color(r, g, b)
    t.forward(count)
    t2.right(90)
    t2.forward(count)
    t.left(200)
    count += 1
    r = (r + 1) % 256
    g = (g + 2) % 256
    b = (b + 3) % 256
    print(count)

# Allows window to stay open
s.mainloop()