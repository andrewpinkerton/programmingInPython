import tkinter as tk
from random import randint
from time import sleep


def main():
    # These are the variables you can change
    number_of_bars = 40
    width = 10
    max_height = 500
    x_pad = 1
    y_pad = 5
    speed = .05
    colors = {
        'background': 'black',
        'unsorted': 'grey',
        'sorted': 'blue',
        'highlight': 'green',
        'best': 'purple',
    }

    # Set up window
    wn = tk.Tk()
    wn.title('Visual Sort')
    wn.config(bg=colors['background'])

    # Move to function: create_bars(args?) -> list
    bars: list = create_bars(number_of_bars, max_height, width, wn, x_pad, y_pad, colors)

    # bubble_sort(bars, colors, x_pad, y_pad, wn, speed)
    # insertion_sort(bars, colors, x_pad, y_pad, wn, speed)
    selection_sort(bars, colors, x_pad, y_pad, wn, speed)

    wn.mainloop()


def create_bars(
        number_of_bars: int, 
        max_height: int, 
        width: int, 
        wn: tk.Tk, 
        x_pad: int, 
        y_pad: int, 
        colors: dict,
) -> list:
    """Creates a list of bars"""
    
    bars = []
    for _ in range(number_of_bars):
        height = randint(1, max_height)
        bar = tk.Frame(wn, width=width, height=height, bg=colors['unsorted'])
        bar.pack(anchor="s", side = "left", padx=x_pad, pady=y_pad)
        bars.append(bar)

    return bars


def bubble_sort(
        bars: list,
        colors: dict,
        x_pad: int,
        y_pad: int,
        wn: tk.Tk,
        speed: float,
) -> None:
    """Perform a bubble sort on the bars."""
   
    for i in range(len(bars)):
        for j in range(len(bars) - 1 - i):
            if bars[j].winfo_reqheight() > bars[j + 1].winfo_reqheight():
                bars[j], bars[j + 1] = bars[j + 1], bars[j]
            bars[j].config(bg=colors['unsorted']) #### Color
            bars[j + 1].config(bg=colors['highlight']) #### Color
            update_bars(bars, x_pad, y_pad, wn, speed)
        bars[-i - 1].config(bg=colors['sorted']) #### Color


def insertion_sort(
        bars: list,
        colors: dict,
        x_pad: int,
        y_pad: int,
        wn: tk.Tk,
        speed: float,
) -> None:
    """Perform an insertion sort on the bars."""

    bars[0].config(bg=colors['sorted']) #### Color
    for j in range(1, len(bars)):
        k = j - 1
        bars[j].config(bg=colors['highlight']) #### Color
        while k >= 0 and bars[k].winfo_reqheight() > bars[k + 1].winfo_reqheight():
            bars[k], bars[k + 1] = bars[k + 1], bars[k]
            k -= 1
            update_bars(bars, x_pad, y_pad, wn, speed)
        bars[k + 1].config(bg=colors['sorted']) #### Color


def selection_sort(
        bars: list,
        colors: dict,
        x_pad: int,
        y_pad: int,
        wn: tk.Tk,
        speed: float,
) -> None:
    """Perform a selection sort on the bars."""

    for k in range(len(bars)):
        best = k

        for q in range(k, len(bars)):
            bars[q].config(bg=colors['highlight'])
            update_bars(bars, x_pad, y_pad, wn, speed)
            if bars[q].winfo_reqheight() < bars[best].winfo_reqheight():
                bars[q].config(bg=colors['best'])
                bars[best].config(bg=colors['unsorted'])
                best = q
            else:
                bars[q].config(bg=colors['unsorted'])
        bars[k], bars[best] = bars[best], bars[k]
        bars[k].config(bg=colors['sorted'])


def repack_bars(
        bars: list, 
        x_pad: int, 
        y_pad: int
) -> None:
    """Repacks the bars"""

    for bar in bars:
        bar.pack_forget()
    for bar in bars:
        bar.pack(anchor="s", side = "left", padx=x_pad, pady=y_pad)


def update_bars(
        bars: list,
        x_pad: int,
        y_pad: int, 
        wn: tk.Tk, 
        speed: float
) -> None:
    """Update bars during each animation"""

    repack_bars(bars, x_pad, y_pad)
    wn.update()
    sleep(speed)


if __name__ == '__main__':
    main()