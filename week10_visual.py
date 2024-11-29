import tkinter as tk
from tkinter.font import Font

from week10_mod import Stack, Queue


def main():
    # Create a window
    window: tk.Tk = tk.Tk()
    window.title("Visualizer")
    font: Font = Font(family="Helvetica", size=14)

    # Frames
    left: tk.Frame = tk.Frame(window)
    right: tk.Frame = tk.Frame(window)

    left.pack(side="left", expand=True, fill="both")
    right.pack(side="right", expand = True, fill="both")

    # Create and do stack stuff: Stack, Labels, Entry, Buttons, and Items
    s: Stack = Stack()
    s_items: tk.Frame = tk.Frame(left)
    s_label: tk.Label = tk.Label(left, text="Stack", font=font)
    s_output: tk.Label = tk.Label(left, text="-", font=font)
    s_entry: tk.Entry = tk.Entry(left, font=font)

    s_label.pack()
    s_output.pack()
    s_entry.pack()

    s_center: CommandCenter = CommandCenter(s, s_items, s_entry, s_output, window, font)

    s_buttons: tk.Frame = tk.Frame(left)
    s_push: tk.Button = tk.Button(s_buttons, text="Push", command=s_center.add_value, font=font)
    s_pop:  tk.Button = tk.Button(s_buttons, text="Pop", command=s_center.remove_value, font=font)
    s_peek:  tk.Button = tk.Button(s_buttons, text="Peek", command=s_center.show_next, font=font)

    s_buttons.pack()
    s_push.pack(side="left")
    s_pop.pack(side="left")
    s_peek.pack(side="left")

    s_items.pack(fill="x")

    # Create and do queue stuff
    q: Queue = Queue()
    q_items: tk.Frame = tk.Frame(right)
    q_label: tk.Label = tk.Label(right, text="Queue", font=font)
    q_output: tk.Label = tk.Label(right, text="-", font=font)
    q_entry: tk.Entry = tk.Entry(right, font=font)

    q_label.pack()
    q_output.pack()
    q_entry.pack()

    q_center: CommandCenter = CommandCenter(q, q_items, q_entry, q_output, window, font)

    q_buttons: tk.Frame = tk.Frame(right)
    q_add: tk.Button = tk.Button(q_buttons, text="Add", command=q_center.add_value, font=font)
    q_remove:  tk.Button = tk.Button(q_buttons, text="Remove", command=q_center.remove_value, font=font)
    q_peek:  tk.Button = tk.Button(q_buttons, text="Peek", command=q_center.show_next, font=font)

    q_buttons.pack()
    q_add.pack(side="left")
    q_remove.pack(side="left")
    q_peek.pack(side="left")

    q_items.pack(fill="x")

    # Keep window open
    window.mainloop()


def update_window(items: list, wn: tk.Tk) -> None:
    """Update the window with the items of the structure."""

    for box in items:
        box.label.pack_forget()
    for box in items:
        box.label.pack(expand=True, fill="both", padx=1, pady=1, anchor="n", side="top")


class CommandCenter:
    """A class to manage the button commands."""

    def __init__(
            self,
            struct: Stack | Queue,
            frame: tk.Frame,
            entry: tk.Entry,
            output: tk.Label,
            wn: tk.Tk,
            font: Font,
    ) -> None:
        """Create a command center."""

        self.struct: Stack | Queue = struct
        self.frame: tk.Frame = frame
        self.entry: tk.Entry = entry
        self.output: tk.Label = output
        self.wn: tk.Tk = wn
        self.font: Font = font

    def add_value(self) -> None:
        """Add a value to the data structure."""

        value: str = self.entry.get()
        box: Box = Box(self.frame, value, self.font)
        self.struct.enter_value(box)

        self.entry.delete(0, tk.END)
        update_window(self.struct.items, self.wn)

    def remove_value(self) -> None:
        """Remove a value from the data structure."""

        if self.struct.is_empty():
            self.output.config(text="Empty")
            return
        
        value: Box = self.struct.get_value()
        value.label.pack_forget()
        self.output.config(text=value)
        update_window(self.struct.items, self.wn)

    def show_next(self) -> None:
        """Show the next value to be removed."""

        if self.struct.is_empty():
            self.output.config(text="Empty")
            return
    
        value: Box = self.struct.view_next()
        self.output.config(text=value)

class Box:
    """A class that represents a box."""

    def __init__(
        self,
        parent: tk.Frame,
        text: str,
        font: Font,
        bg_color: str="black",
        fg_color: str="white",
    ) -> None:
        """Create a new box class."""

        self.text: str = text
        self.label: tk.Label = tk.Label(
            parent,
            text=self.text,
            font=font,
            bg=bg_color,
            fg=fg_color,
        )

    def __str__(self) -> str:
        """Pretty print"""

        return self.text
        

if __name__ == "__main__":
    main()