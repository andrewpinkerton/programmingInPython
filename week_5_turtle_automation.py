import csv
import turtle as tg


def main():
    t = tg.Turtle()
    s = tg.Screen()

    with open('Programming in Python/week 5/moves.csv') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            method = row[0]
            command = row[1]
            
            if method == 'bgcolor':
                s.bgcolor(command)
            elif method == 'color':
                t.color(command)
            elif method == 'forward':
                t.forward(int(command))
            elif method == 'backward':
                t.backward(int(command))
            elif method == 'left':
                t.left(int(command))
            elif method == 'right':
                t.right(int(command))


    s.mainloop()
 
if __name__ == "__main__":
    main()