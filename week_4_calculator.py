import tkinter as tk
from tkinter.font import Font

def main():
    wn = tk.Tk()
    wn.title("Calculator")

    font_style = Font(family="Courier", size = 20)
    result_style = Font(family="Courier", size = 50)

    entry_exp = tk.Entry(master=wn, width=30, font=font_style)
    label_eq = tk.Label(master=wn, text=" = ", font=font_style)
    label_result = tk.Label(master=wn, text="0", font=result_style)
    button_calc = tk.Button(
        master=wn, 
        text="Calculate", 
        font=font_style,
        command=lambda : calculate(entry_exp, label_result)
        )

    entry_exp.grid(row=0, column=0)
    label_eq.grid(row=0, column=1)
    label_result.grid(row=1)
    button_calc.grid(row=2)

    wn.mainloop()

def calculate(entry_obj, label_result):
    expression = entry_obj.get()
    result = eval(expression)
    label_result["text"] = result
 
if __name__ == "__main__":
    main()