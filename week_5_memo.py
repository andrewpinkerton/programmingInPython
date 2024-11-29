import tkinter as tk


def main():
    width = 500
    height = 300
    widgets_width = 40

    # Colors: customize if you want
    colors = {
        "console_color": "dark blue",
        "console_text_color": "yellow",
        "background_color": "dark gray",
        "main_text_color": "black",
    }

    #Font
    font_family = "Comic Sans"

    #Main part of code
    wn = tk.Tk()
    wn.title("Hacker's Memo")
    wn.geometry(f"{width}x{height}")
    wn.minsize(width, height)
    wn.config(bg=colors["background_color"])

    label = tk.Label(
        wn,
        text = "Hacker's Memo",
        bg=colors["background_color"],
        fg=colors["main_text_color"],
        font=(font_family, 20)
    )
    label.pack()

    entry_text = tk.Text(wn, height=10, width=widgets_width)
    entry_text.config(
        fg=colors["console_text_color"],
        bg=colors["console_color"],
        insertbackground=colors["console_text_color"]
    )
    entry_text.pack()

    button_add = tk.Button(
        wn,
        text="Add",
        width=widgets_width + 5,
        fg=colors["main_text_color"],
        bg=colors["background_color"],
        command=lambda: add_to_file(entry_text), 
    )
    button_add.pack()

    button_clear_screen = tk.Button(
        wn,
        text="Clear Screen",
        width=widgets_width + 5,
        fg=colors["main_text_color"],
        bg=colors["background_color"],
        command=lambda: clear_screen(entry_text), 
    )
    button_clear_screen.pack()

    button_clear_file = tk.Button(
        wn,
        text="Clear File",
        width=widgets_width + 5,
        fg=colors["main_text_color"],
        bg=colors["background_color"],
        command=lambda: clear_file(entry_text), 
    )
    button_clear_file.pack()

    wn.mainloop()

def add_to_file(entry_text):
    text = entry_text.get("1.0", "end")
    with open("Programming in Python\week 5\memo.txt", "a") as f:
        f.write(text)
    print("Added to file")

def clear_screen(entry_text):
    entry_text.delete("1.0", "end")
    print("Screen cleared")

def clear_file(entry_text):
    with open("Programming in Python\week 5\memo.txt", "w") as f:
            f.write("")
    entry_text.delete("1.0", "end")
    entry_text.insert("1.0", "The file has been cleared.\nPress 'Clear Screen'")
    print("File Cleared")


if __name__ == "__main__":
    main()