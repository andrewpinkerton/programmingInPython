import tkinter as tk
from tkinter.font import Font
import tkinter.filedialog
import tkinter.messagebox
import os
import shutil

from send2trash import send2trash


def main():
    # Custom Variables
    button_size_x: int = 40
    button_size_y: int = 3
    font_size: int = 30

    # Window Setup
    wn: tk.Tk = tk.Tk()
    wn.title("File Automation")

    # Frame for widgets
    frame: tk.Frame = tk.Frame(
        wn,
        padx=20,
        pady=20,
        bg=ColorPalette.background_color,
    )
    frame.pack()

    # Create Labels
    label: tk.Label = tk.Label(
        frame,
        text="File Automation",
        bg=ColorPalette.background_color,
        fg=ColorPalette.text_color,
        font=Font(size=font_size),
    )
    label.pack()

    # Create buttons
    copy_button: CustomButton = CustomButton(
        master=frame,
        text="Copy File",
        width=button_size_x,
        height=button_size_y,
        command=copy_file,
    )
    copy_button.pack()

    move_button: CustomButton = CustomButton(
        master=frame,
        text="Move File",
        width=button_size_x,
        height=button_size_y,
        command=move_file,
    )
    move_button.pack()

    rename_button: CustomButton = CustomButton(
        master=frame,
        text="Rename File",
        width=button_size_x,
        height=button_size_y,
        command=rename_file,
    )
    rename_button.pack()

    delete_button: CustomButton = CustomButton(
        master=frame,
        text="Delete File",
        width=button_size_x,
        height=button_size_y,
        command=delete_file,
    )
    delete_button.pack()

    # Keep window open
    wn.mainloop()


def copy_file() -> None:
    """Make a copy of a file."""

    tk.messagebox.showinfo("Alert", "Please select a file to copy.")
    base_file = tk.filedialog.askopenfilename()
    base_file_name = os.path.basename(base_file)

    new_file_name = f"copy_of_{base_file_name}"

    tk.messagebox.showinfo("Alert", "Please select a destination to copy into.")
    destination = tk.filedialog.askdirectory()

    destination_path = os.path.join(destination, new_file_name)

    shutil.copy(base_file, destination_path)
    tk.messagebox.showinfo("Success", "File copied succesfully.")


def move_file() -> None:
    """Move a file to a different directory."""

    tk.messagebox.showinfo("Alert", "Please select a file to be moved.")
    base_file = tk.filedialog.askopenfilename()

    tk.messagebox.showinfo("Alert", "Please select a destination to move into.")
    destination = tk.filedialog.askdirectory()

    if (os.path.dirname(base_file) == destination):
        tk.messagebox.showinfo("Error", "File is being moved into the same directory.")
        return

    shutil.move(base_file, destination)
    tk.messagebox.showinfo("Success", "File moved succesfully.")


def rename_file() -> None:
    """Rename a file."""

    tk.messagebox.showinfo("Alert", "Please select a file to rename.")
    file_path = tk.filedialog.askopenfilename()

    directory = os.path.dirname(file_path)
    original_file_name = os.path.basename(file_path)

    new_file_name = tk.simpledialog.askstring("Rename", "Enter the new name for the file with the correct extension:")

    if new_file_name == original_file_name:
        tk.messagebox.showerror("Error", "The new file name is the same as the original.")
        return
    
    new_file_path = os.path.join(directory, new_file_name)

    os.rename(file_path, new_file_path)
    tk.messagebox.showinfo("Success", "File renamed successfully.")


def delete_file() -> None:
    """Delete a file and sent it to the trash."""

    tk.messagebox.showinfo("Alert", "Please select a file to delete.")
    file_path = tk.filedialog.askopenfilename()

    confirm = tk.messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the file: {os.path.basename(file_path)}?")

    if confirm == True:
        absolute_path = os.path.abspath(file_path)
        send2trash(absolute_path)
        tk.messagebox.showinfo("Success", "File sent to the trash successfully.")
    else:
        tk.messagebox.showinfo("Cancelled", "File deletion was cancelled.")


class CustomButton(tk.Button):
    """A class to create buttons with hover effects."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.config(
            bg=ColorPalette.base_button_color,
            fg=ColorPalette.text_button_color,
        )
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.off_hover)

    def on_hover(self, event: tk.Event) -> None:
        """Change the color of the button when the mouse hovers over it."""

        event.widget.config(bg=ColorPalette.hover_button_color)

    def off_hover(self, event: tk.Event) -> None:
        """Change the color of the button when the mouse moves off button."""

        event.widget.config(bg=ColorPalette.base_button_color)


class ColorPalette:
    """A class to store color codes for the GUI."""

    background_color: str = "black"
    text_color: str = "white"

    base_button_color: str = "SystemButtonFace"
    hover_button_color: str = "cyan"
    text_button_color: str = "black"


if __name__ == "__main__":
    main()