import tkinter as tk
from tkinter import filedialog
import re

def main():
    font = ("Consolas", 30)
    bg_color = "black"

    wn = tk.Tk()
    wn.title("Capture the Flag")
    wn.geometry("700x150")
    wn.configure(bg=bg_color)


    # Top Section
    top_frame = tk.Frame(wn, bg=bg_color, padx=10, pady=10)
    top_frame.pack(side = "top", anchor = "w", fill="both")

    flag_label = tk.Label(
        top_frame,
        text="Flag:",
        font=font,
        bg=bg_color,
        fg="white",
    )
    flag_label.pack(side = "left")

    flag_value_label = tk.Label(
        top_frame,
        text="EXAMPLE",
        font=font,
        bg=bg_color,
        fg="limegreen",
    )
    flag_value_label.pack(side="left")

    # Bottom Section
    bottom_frame = tk.Frame(wn, bg=bg_color, padx=10, pady=10)
    bottom_frame.pack(fill="both")

    search_button = tk.Button(
        bottom_frame,
        text = "FIND",
        font=font,
        command=lambda: find_flag(flag_value_label),
    )
    search_button.pack(fill="both")

    wn.mainloop()


def find_flag(result_label: tk.Label) -> None:
    """Find FLAG in file and update Label with result"""

    filename = filedialog.askopenfilename()

    with open(filename) as f:
        content = f.read()

    flag_pattern = r"(FLAG(-{1,3}|>{1,2})\w*(-{1,3}|<{1,2}))"
    matches: list = re.findall(flag_pattern, content)

    if matches:
        result_label.config(text=matches[0][0])
    else:
        result_label.config(text="No Flag Found!")

    result_label.pack(side="left")


if __name__ == "__main__":
    main()