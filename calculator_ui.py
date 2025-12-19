import tkinter as tk
from tkinter import END, INSERT, Event, StringVar, ttk
import calculator as calculator

calc = calculator.Calculator()
target_operation = None

def process_keypress(event):
    calc_input(event.keysym)

def calc_input(keysym):
    num = calc.current_value

    # Handle input
    if keysym == 'BackSpace':
        num = num[:-1]
        if (num == ""):
            num = '0'
    elif keysym == 'period':
        if '.' not in num:
            num += '.'
    elif keysym.isdigit():
        if num == "0" and keysym == '0':
            return
        num += keysym
    
    # Strip leading zeros
    if (num != "0" and "." not in num):
        num = num.lstrip("0")

    # Format string
    if '.' in num:
        num_format = num.replace(",", "")
        dec_split = num_format.split(".")
        calc.current_value = f"{int(dec_split[0]):,}" + '.'
        if len(dec_split) == 2:
            calc.current_value += dec_split[1]
    else:
        num_format = num.replace(",", "")
        calc.current_value = f"{int(num_format):,}"

    # Insert string into entry field, then set back to read-only
    visible_field.config(state="normal")
    visible_field.delete(0, tk.END)
    visible_field.insert(0, calc.current_value)
    visible_field.config(state="readonly")
    return

def set_target_op(operation):
    target_operation = operation

def clear_entry():
    calc.current_value = "0"
    visible_field.config(state="normal")
    visible_field.delete(0, tk.END)
    visible_field.insert(0, "0")
    visible_field.config(state="readonly")

def all_clear():
    clear_entry()
    calc.all_clear()

calc_operation = [
    ["%", calc.modulo],
    ["CE", clear_entry],
    ["C", all_clear],
    ["⌫", lambda: calc_input('BackSpace')],

    ["¹/𝑥", None],
    ["xʸ", lambda: set_target_op(calc.exponent)],
    ["ʸ√𝑥", lambda: set_target_op(calc.root_extration)],
    ["÷", lambda: set_target_op(calc.division)],
    
    ["7", lambda: calc_input('7')],
    ["8", lambda: calc_input('8')],
    ["9", lambda: calc_input('9')],
    ["×", lambda: set_target_op(calc.multiplication)],
    
    ["4", lambda: calc_input('4')],
    ["5", lambda: calc_input('5')],
    ["6", lambda: calc_input('6')],
    ["-", lambda: set_target_op(calc.subtraction)],
    
    ["1", lambda: calc_input('1')],
    ["2", lambda: calc_input('2')],
    ["3", lambda: calc_input('3')],
    ["+", lambda: set_target_op(calc.addition)],

    ["⁺∕₋", None],
    ["0", lambda: calc_input('0')],
    [".", lambda: calc_input('period')],
    ["=", None]
]

root = tk.Tk()
root.title("Calculator")
root.configure(background='#1E1E1E')
root.geometry('450x600')

root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)

frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky = tk.NSEW)

style = ttk.Style()
style.theme_use('clam')
style.configure("TFrame", background="#1E1E1E")
style.configure("TLabel", padding=6,foreground="#D4D4D4", background="#1E1E1E")
style.configure("BG.TLabel", padding=6, relief="flat5", foreground="#D4D4D4", background="#1E1E1E")
style.configure("Ent.TLabel", padding=6, relief="flat5", foreground="#D4D4D4", background="#1E1E1E", insertcolor = "#1E1E1E")
style.configure("Btn.TLabel", padding=6, relief="flat5", foreground="#D4D4D4", background="#444", anchor = tk.CENTER, font=("Helvetica 14"))
style.map("Btn.TLabel", background=[('pressed', '!disabled', '#666'), ('active', '#4D4D4D')])

frame.rowconfigure(0, weight = 1)
frame.columnconfigure(0, weight = 1)

visible_field_sv = StringVar()
ttk.Label(frame, style="BG.TLabel", justify = tk.RIGHT).grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=2,
    pady=2
)
visible_field = ttk.Entry(frame, style="Ent.TLabel", justify = tk.RIGHT, font=("Helvetica 32 bold"))
visible_field.insert(0,"0")
visible_field.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=20,
    pady=25
)
visible_field.config(state='readonly')

visible_field.focus_set()

for row in range(1, 7):
    frame.rowconfigure(row, weight = 1)
    for col in range(4):
        frame.columnconfigure(col, weight = 1)
        ttk.Button(
            frame,
            text=calc_operation[col + (row - 1) * 4][0],
            style="Btn.TLabel",
            command=calc_operation[col + (row - 1) * 4][1]
        ).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

root.bind("<Key>", process_keypress)

root.resizable(True, True)

root.mainloop()