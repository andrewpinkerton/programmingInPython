import tkinter as tk
from random import randint
from time import sleep

def main():
    number_of_bars = 40
    width = 10
    max_height = 500
    x_pad = 1
    y_pad = 5
    speed = .01

    colors = {
        "background": "black",
        "unsorted": "grey",
        "sorted": "limegreen",
        "highlight": "blue"
    }

    wn = tk.Tk()
    wn.title("Visual Sort")
    wn.config(bg=colors["background"])

    bars = []
    for _ in range(number_of_bars):
        height: int = randint(2, max_height)
        bar = tk.Frame(wn, width=width, height=height, bg=colors["unsorted"])
        bar.pack(anchor="s", side="left", padx=x_pad, pady=y_pad)
        bars.append(bar)


    # # Bubble Sort
    # for i in range(len(bars)):
    #     for j in range(len(bars) - 1 - i):
    #         if bars[j].winfo_reqheight() > bars[j + 1].winfo_reqheight():
    #             bars[j], bars[j + 1] = bars[j + 1], bars[j]
    #         bars[j].config(bg=colors["unsorted"]) ### Color
    #         bars[j + 1].config(bg=colors["highlight"]) ### Color
    #         repack_bars(bars, x_pad, y_pad)
    #         wn.update()
    #         sleep(speed)
    #     bars[-i - 1].config(bg=colors["sorted"]) ### Color

    #Insertion Sort
    bars[0].config(bg=colors["sorted"]) # because first is sorted already
    for i in range(1, len(bars)):
        k = i - 1
        while k >=0 and bars[k].winfo_reqheight() > bars[k+1].winfo_reqheight():
            bars[k], bars[k+1] = bars[k+1], bars[k]
            k -=1
            bars[k+1].config(bg=colors["highlight"]) #current tracker
            repack_bars(bars,x_pad, y_pad)
            wn.update()
            sleep(speed)
        bars[k+1].config(bg=colors["sorted"]) #sorted tracker

    wn.mainloop()


def repack_bars(bars, x_pad, y_pad):
    for bar in bars:
        bar.pack_forget()
    for bar in bars:
        bar.pack(anchor="s", side="left", padx=x_pad, pady=y_pad)

if __name__ == "__main__":
    main()