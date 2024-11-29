# Imports
import tkinter as tk
from random import randint
from time import sleep


# Main Function
def main():
    # Variables to change
    number_of_bars:int = 20
    width:int = 10
    max_height:int = 500
    spacing: int = 1
    speed: float = .01

    # Window Setup
    wn: tk.Tk = tk.Tk()
    wn.title('Visual Sort')
    wn.config(bg=Color.BACKGROUND)

    # Create Bars
    bars: Bars = Bars(wn, spacing, speed)
    bars.create_bars(number_of_bars, width, max_height, Color.UNSORTED)

    # Sorts
    bars.insertion_sort()
    bars.clear_bars()
    sleep(1)
    bars.create_bars(number_of_bars, width, max_height, Color.UNSORTED)
    bars.selection_sort()
    bars.clear_bars()
    sleep(1)
    bars.create_bars(number_of_bars, width, max_height, Color.UNSORTED)
    bars.bubble_sort()

    wn.mainloop()


# Color
class Color:
    """An enum class with colors."""

    BACKGROUND = "black"
    UNSORTED = "grey"
    SORTED = "limegreen"
    HIGHLIGHT = "yellow"
    BEST = "blue"


# Bars
class Bars:
    """Bars class with a list of bars and methods to create and sort them."""

    def __init__(self, wn: tk.Tk, spacing: int, speed: float) -> None:
        """Create a new set of bars to sort."""

        self.wn: tk.Tk = wn
        self.spacing: int = spacing
        self.speed: float = speed
        self.bars: list[Bar] = []
    
    def create_bars(
        self,
        number_of_bars: int,
        width: int,
        max_height: int,
        color: str,
    ) -> None:
        """Create random height bars and store int self.bars"""

        for _ in range(number_of_bars):
            height: int = randint(1, max_height)
            bar: Bar = Bar(height, width, color, self.wn)
            self.bars.append(bar)
        self.pack_bars()

    def pack_bars(self) -> None:
        """Pack the bars into the window."""

        for bar in self.bars:
            bar.frame.pack(side= "left", anchor="s", padx=self.spacing, pady=self.spacing)

    def update_bars(self) -> None:
        """Update the bars in the window."""

        for bar in self.bars:
            bar.frame.pack_forget()
        self.pack_bars()
        self.wn.update()
        sleep(self.speed)

    def clear_bars(self) -> None:
        """Clear the bars from the window."""

        for bar in self.bars:
            bar.frame.pack_forget()
        self.bars = []

    def insertion_sort(self) -> None:
        """Sort the bars using the insertion sort algorithm"""

        self.bars[0].color(Color.SORTED)
        for j in range(1, len(self.bars)):
            k: int = j - 1
            self.bars[j].color(Color.HIGHLIGHT)
            while k >= 0 and self.bars[k] > self.bars[k+1]:
                self.bars[k], self.bars[k+1] = self.bars[k+1], self.bars[k]
                k-=1
                self.update_bars()
            self.bars[k+1].color(Color.SORTED)
            self.update_bars()
        self.update_bars()

    def selection_sort(self) -> None:
        """Sort the bars using the selection sort algorithm"""

        for k in range(len(self.bars)):
            best = k
            for q in range(k, len(self.bars)):
                self.bars[q].color(Color.HIGHLIGHT)
                self.update_bars()
                if self.bars[q].height < self.bars[best].height:
                    self.bars[best].color(Color.UNSORTED) #### Color
                    self.bars[q].color(Color.BEST) #### Color
                    best = q
                else:
                    self.bars[q].color(Color.UNSORTED) #### Color
            self.bars[k], self.bars[best] = self.bars[best], self.bars[k]
            self.bars[k].color(Color.SORTED) #### Color
            self.update_bars()
        self.update_bars()

    def bubble_sort(self) -> None:
        """Sort the bars using the bubble sort algorithm"""

        for i in range(len(self.bars)):
            for j in range(len(self.bars) - 1 - i):
                if self.bars[j].height > self.bars[j + 1].height:
                    self.bars[j], self.bars[j + 1] = self.bars[j + 1], self.bars[j]
                self.bars[j].color(Color.UNSORTED) #### Color
                self.bars[j + 1].color(Color.HIGHLIGHT) #### Color
                self.update_bars()
            self.bars[-i - 1].color(Color.SORTED) #### Color
            self.update_bars()
        self.update_bars()


# Bar
class Bar:
    """Bar class with a height and color."""

    def __init__(self, height: int, width: int, color: str, wn: tk.Tk) -> None:
        """Create a new bar with a height and color"""

        self.height: int = height
        self.frame: tk.Frame = tk.Frame(wn, width=width, height=height, bg=color)

    def color(self, color: str) -> None:
        """Change color of bar."""

        self.frame.config(bg=color)

    def __gt__(self, other: object) -> bool:
        """Return true if greater than other, false otherwise."""

        return self.height > other.height
    
    def __lt__(self, other: object) -> bool:
        """Return true if less than other, false otherwise."""

        return self.height < other.height

    def __str__(self) -> str:
        """Return pretty string."""

        return str(self.height)
    
    def __repr__(self) -> str:
        """Represent self."""

        return str(self.height)


if __name__ == "__main__":
    main()