import re
import tkinter as tk
from tkinter import END, INSERT, StringVar, ttk 
from time import strftime
import calculator as calculator

calc = calculator.Calculator()

calc_operation = [
    ["%", None],
    ["CE", None],
    ["C", None],
    ["⌫", None],

    ["¹/𝑥", calc.modulo],
    ["xʸ", calc.exponent],
    ["ʸ√𝑥", calc.root_extration],
    ["÷", calc.division],
    
    ["7", None],
    ["8", None],
    ["9", None],
    ["×", calc.multiplication],
    
    ["4", None],
    ["5", None],
    ["6", None],
    ["-", calc.subtraction],
    
    ["1", None],
    ["2", None],
    ["3", None],
    ["+", calc.addition],

    ["⁺∕₋", None],
    ["0", None],
    [".", None],
    ["=", None]
]

#def formatCalcEntry(entry, calculator):

def calc_input(event):
    visible_field.config(state="normal")
    visible_field.delete(0, tk.END)
    visible_field.insert(0, event.keysym)
    visible_field.config(state="readonly")
    return

def formatCalcEntry(a, b, c):
    input_decimal = visible_field.get().replace(",", "")

    #try:
    #    calc.current_value = float(input_decimal)
    #except ValueError:
    #    pass

    try:
        pattern = r"^\d*\.?\d*$"
        if re.fullmatch(pattern, input_decimal):
            if (input_decimal == "."):
                input_decimal = "0."
            calc.current_value = input_decimal.lstrip("0") if "." not in input_decimal else input_decimal
    except ValueError:
        pass
    
    if (calc.current_value == ""):
        visible_field_sv.set("0")
    else:
        visible_field_sv.set(calc.current_value)

    #visible_field.insert("insert", END)

    #entry.delete(0,END)
    #entry.insert(0,"ss")
    #visible_field_sv.set("ss")
    #visible_field_sv.set(f"{calc.current_value:,}")
    #entry.insert(0,f"{calculator.current_value:,}")
    return

#def testVal(inStr, acttyp):
#    if acttyp == '1': #insert
#        if not inStr.isdigit():
#            return False
#    return True

def clear_entry():
    print()

def all_clear():
    print()

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

#entry_field_sv = StringVar()
#entry_field = ttk.Entry(frame, validate="key", textvariable=entry_field_sv, takefocus=True)

visible_field_sv = StringVar()
ttk.Label(frame, style="BG.TLabel", justify = tk.RIGHT).grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=2,
    pady=2
)
visible_field = ttk.Entry(frame, text="0", style="Ent.TLabel", justify = tk.RIGHT, font=("Helvetica 32 bold"))
#visible_field = ttk.Entry(frame, text="0", style="Ent.TLabel", justify = tk.RIGHT, font=("Helvetica 32 bold"), validate="key", textvariable=visible_field_sv, state='readonly')
visible_field.insert(0,"ss")
    #visible_field.insert("insert", END)
visible_field.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=20,
    pady=25
)
visible_field.config(state='readonly')

#visible_field_sv.trace("w", formatCalcEntry)

#visible_field_sv.trace("w", lambda visible_field, calc, visible_field_sv=visible_field_sv:formatCalcEntry(visible_field, calc))
#visible_field['validatecommand'] = (visible_field.register(testVal),'%P','%d')

visible_field.focus_set()

for row in range(1, 7):
    frame.rowconfigure(row, weight = 1)
    for col in range(4):
        frame.columnconfigure(col, weight = 1)
        _btn = ttk.Button(
            frame,
            #text=f"Cell ({row}, {col})",
            text=calc_operation[col + (row - 1) * 4][0],
            style="Btn.TLabel"
        ).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

#Button(root, text="Span 2 columns", style="Btn.TLabel").grid(
#    row=3,
#    column=0,
#    columnspan=2,
#    sticky="ew",
#)
#Button(root, text="Span 2 rows", style="Btn.TLabel").grid(
#    row=4,
#    column=0,
#    rowspan=2,
#    sticky="ns",
#)

#root.geometry('250x100')

#Label(root, text = 'It\'s resizable').pack(side = tk.TOP, pady = 10)

# Allowing root window to change
# it's size according to user's need

root.bind("<KeyRelease>", calc_input)

root.resizable(True, True)

root.mainloop()