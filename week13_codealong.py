import tkinter as tk
from tkinter.font import Font


def main():
    wn: tk.Tk = tk.Tk()
    wn.title("Base Converter")
    font_style: Font = Font(family="Consolas", size=20)
    wn.configure(bg=Colors.background)

    # Widgets
    number_entry: tk.Entry = tk.Entry(
        wn,
        font=font_style,
        bg=Colors.foreground,
        fg=Colors.text,
    )

    choices: tuple = ("Binary", "Octal", "Decimal", "Hexadecimal")
    base_input_sbox: tk.Spinbox = tk.Spinbox(
        wn,
        values=choices,
        state="readonly",
        font=font_style,
        buttonbackground=Colors.foreground,
        readonlybackground=Colors.foreground,
        fg=Colors.text,
    )
    base_output_sbox: tk.Spinbox = tk.Spinbox(
        wn,
        values=choices,
        state="readonly",
        font=font_style,
        buttonbackground=Colors.foreground,
        readonlybackground=Colors.foreground,
        fg=Colors.text,
    )

    result_label: tk.Label = tk.Label(
        wn,
        text="-",
        font=font_style,
        bg=Colors.background,
        fg=Colors.text,
    )

    commmand_center: CommandCenter = CommandCenter(
        number_entry,
        base_input_sbox,
        base_output_sbox,
        result_label,
    )
    convert_button: tk.Button = tk.Button(
        wn,
        text="Convert",
        command=commmand_center.convert,
        font=font_style,
        bg=Colors.background,
        fg=Colors.text,
        activebackground=Colors.text,
        activeforeground=Colors.background,
    )

    logo: tk.PhotoImage = tk.PhotoImage(master=wn, file="logo.png")
    logo = logo.subsample(2)
    logo_label: tk.Label = tk.Label(wn, image=logo, bg=Colors.background)

    # Packing area
    px: int = 10
    py: int = 5
    number_entry.pack(fill="x", padx=px, pady=py)
    base_input_sbox.pack(fill="x", padx=px, pady=py)
    base_output_sbox.pack(fill="x", padx=px, pady=py)
    result_label.pack(fill="x", padx=px, pady=py)
    convert_button.pack(fill="x", padx=px, pady=py)
    logo_label.pack(fill="x", padx=px, pady=py)

    wn.mainloop()


class CommandCenter:
    """CommandCenter class for handling button commands."""

    def __init__(
        self,
        entry: tk.Entry,
        input_base: tk.Spinbox,
        output_base: tk.Spinbox,
        output: tk.Label,
    ) -> None:
        """Initialize CommandCenter with widgets."""

        self.entry: tk.Entry = entry
        self.input_base: tk.Spinbox = input_base
        self.output_base: tk.Spinbox = output_base
        self.output: tk.Label = output

    def convert(self) -> None:
        """Convert input number from input base to output base and display """

        number_input: str = self.entry.get()
        input_base: str = self.input_base.get()
        output_base: str = self.output_base.get()

        # Convert input base to decimal
        try:
            if input_base == "Binary":
                number: int = int(number_input, 2)
            if input_base == "Octal":
                number: int = int(number_input, 8)
            if input_base == "Decimal":
                number: int = int(number_input, 10)
            if input_base == "Hexadecimal":
                number: int = int(number_input, 16)
        except ValueError:
            self.output.config(text="Invalid Number")
            return

        # Convert number to output base
        if output_base == "Binary":
            number_output: str = bin(number)[2:]
        if output_base == "Octal":
            number_output: str = oct(number)[2:]
        if output_base == "Decimal":
            number_output: str = str(number)
        if output_base == "Hexadecimal":
            number_output: str = hex(number)[2:]

        self.output.config(text=number_output)
        

class Colors:
    """Color class for storing colors."""

    background: str = "#222222"
    foreground: str = "#444444"
    text: str = "#f59342"


if __name__ == "__main__":
    main()