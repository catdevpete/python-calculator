import tkinter as tk
from tkinter import END, INSERT, Event, StringVar, ttk
import calculator
import calc_icon as ico
import os

class Calculator_GUI:
    calc = calculator.Calculator()
    entry = None
    current_value = "0"
    target_operation = None
    setting_operation = False
    input_after_op_set = False
    performed_equal = False
    calc_operation = []

    def __init__(self):
        self.calc = calculator.Calculator()
        self.current_value = "0"
        self.target_operation = None
        self.input_after_op_set = None
        self.setting_operation = False
        self.performed_equal = False

        self.calc_operation = [
        ["%",   "ButtonOps.TLabel",    lambda: self.set_target_op(self.calc.modulo)],
        ["CE",  "ButtonOps.TLabel",    lambda: self.clear_entry()],
        ["C",   "ButtonOps.TLabel",    lambda: self.all_clear()],
        ["⌫",  "ButtonOps.TLabel",    lambda: self.calc_input('BackSpace')],

        ["¹/𝑥", "ButtonOps.TLabel",    lambda: self.perform_one_over_x()],
        ["𝑥ʸ",  "ButtonOps.TLabel",    lambda: self.set_target_op(self.calc.exponent)],
        ["ʸ√𝑥", "ButtonOps.TLabel",    lambda: self.set_target_op(self.calc.root_extration)],
        ["÷",   "ButtonOps.TLabel",    lambda: self.set_target_op(self.calc.division)],

        ["7",   "ButtonDigits.TLabel", lambda: self.calc_input('7')],
        ["8",   "ButtonDigits.TLabel", lambda: self.calc_input('8')],
        ["9",   "ButtonDigits.TLabel", lambda: self.calc_input('9')],
        ["×",   "ButtonOps.TLabel",    lambda: self.set_target_op(self.calc.multiplication)],
  
        ["4",   "ButtonDigits.TLabel", lambda: self.calc_input('4')],
        ["5",   "ButtonDigits.TLabel", lambda: self.calc_input('5')],
        ["6",   "ButtonDigits.TLabel", lambda: self.calc_input('6')],
        ["-",   "ButtonOps.TLabel",    lambda: self.set_target_op(self.calc.subtraction)],

        ["1",   "ButtonDigits.TLabel", lambda: self.calc_input('1')],
        ["2",   "ButtonDigits.TLabel", lambda: self.calc_input('2')],
        ["3",   "ButtonDigits.TLabel", lambda: self.calc_input('3')],
        ["+",   "ButtonOps.TLabel",    lambda: self.set_target_op(self.calc.addition)],

        ["⁺∕₋", "ButtonDigits.TLabel", lambda: self.toggle_negative()],
        ["0",   "ButtonDigits.TLabel", lambda: self.calc_input('0')],
        [".",   "ButtonDigits.TLabel", lambda: self.calc_input('period')],
        ["=",   "ButtonEqual.TLabel",  lambda: self.equal_operation()]
    ]
        
    def set_entry(self, entry):
        self.entry = entry
        
    def set_entry_value(self, value):
        # Insert string into entry field, then set back to read-only
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)
        self.entry.config(state="readonly")

    def process_keypress(self, event):
        self.calc_input(event.keysym)

    def set_input_after(self):
        if self.setting_operation:
            self.input_after_op_set = True

    def calc_input(self, keysym):
        if self.performed_equal == True:
            self.current_value = "0"
            self.performed_equal = False

        num = self.current_value

        # Handle input
        if keysym == 'BackSpace':
            num = num[:-1]
            if (num == ""):
                num = '0'
            self.set_input_after()
        elif keysym == 'period':
            if '.' not in num:
                num += '.'
            self.set_input_after()
        elif keysym.isdigit():
            if num == "0" and keysym == '0':
                return
            num += keysym
            self.set_input_after()

        # Strip leading zeros
        if (num != "0" and "." not in num):
            num = num.lstrip("0")

        # Format string
        if '.' in num:
            num_format = num.replace(",", "")
            dec_split = num_format.split(".")
            self.current_value = f"{int(dec_split[0]):,}" + '.'
            if len(dec_split) == 2:
                self.current_value += dec_split[1]
        else:
            num_format = num.replace(",", "")
            self.current_value = f"{int(num_format):,}"

        self.set_entry_value(self.current_value)
        return

    def toggle_negative(self):
        if '-' in self.current_value:
            self.current_value = self.current_value.replace('-', "")
        else:
            self.current_value = '-' + self.current_value

        self.set_entry_value(self.current_value)
        self.set_input_after()

    def set_target_op(self, operation):
        if not self.setting_operation:
            if not self.input_after_op_set:
                self.setting_operation = True
                self.calc.cache_value = float(self.current_value.replace(",", ""))
                self.current_value = "0"
        else:
            if self.input_after_op_set:
                self.current_value = str(self.calc.perform_operation(float(self.current_value.replace(",", "")), self.target_operation))
                self.set_entry_value(self.current_value)
                self.setting_operation = True
                self.input_after_op_set = False
                self.current_value = "0"

        self.performed_equal = False
        self.target_operation = operation
        return

    def perform_one_over_x(self):
        self.calc.cache_value = 1.0
        self.current_value = str(self.calc.perform_operation(float(self.current_value.replace(",", "")), self.calc.division))
        self.set_entry_value(self.current_value)
        self.setting_operation = False
        self.input_after_op_set = False
        self.performed_equal = True
    
    def clear_entry(self):
        self.current_value = "0"
        self.set_entry_value("0")

    def all_clear(self):
        self.clear_entry()
        self.calc.all_clear()

    def equal_operation(self):
        if self.setting_operation and self.input_after_op_set:
            self.current_value = str(self.calc.perform_operation(float(self.current_value.replace(",", "")), self.target_operation))
            self.set_entry_value(self.current_value)
            self.setting_operation = False
            self.input_after_op_set = False
            self.performed_equal = True


if __name__ == "__main__":
    calc_ui = Calculator_GUI()
    root = tk.Tk()
    root.title("Calculator")
    root.configure(background='#1E1E1E')
    root.geometry('450x600')

    root.iconbitmap(ico.Icon().tempFile)
    os.remove(ico.Icon().tempFile)

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
    style.configure("ButtonDigits.TLabel", padding=6, relief="flat5", foreground="#D4D4D4", background="#555", anchor = tk.CENTER, font=("Helvetica 14"))
    style.configure("ButtonOps.TLabel", padding=6, relief="flat5", foreground="#D4D4D4", background="#333", anchor = tk.CENTER, font=("Helvetica 14"))
    style.configure("ButtonEqual.TLabel", padding=6, relief="flat5", foreground="#555", background="#C6EBFA", anchor = tk.CENTER, font=("Helvetica 14"))
    style.map("ButtonDigits.TLabel", background=[('pressed', '!disabled', '#666'), ('active', '#4D4D4D')])
    style.map("ButtonOps.TLabel", background=[('pressed', '!disabled', '#666'), ('active', '#4D4D4D')])
    style.map("ButtonEqual.TLabel", background=[('pressed', '!disabled', '#666'), ('active', "#B3D5E2")])

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
    calc_ui.set_entry(visible_field)

    for row in range(1, 7):
        frame.rowconfigure(row, weight = 1)
        for col in range(4):
            frame.columnconfigure(col, weight = 1)
            button = ttk.Button(
                frame,
                text=calc_ui.calc_operation[col + (row - 1) * 4][0],
                style=calc_ui.calc_operation[col + (row - 1) * 4][1]
            )
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            button.configure(command=calc_ui.calc_operation[col + (row - 1) * 4][2])
            

    root.bind("<Key>", calc_ui.process_keypress)
    root.resizable(True, True)

    root.mainloop()