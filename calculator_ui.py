import tkinter as tk
from tkinter import ttk 
from time import strftime
import calculator as calculator

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

root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)

frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky = tk.NSEW)

style = ttk.Style()
style.theme_use('clam')
style.configure("TFrame", background="#1E1E1E")
style.configure("TLabel", padding=6,foreground="#D4D4D4", background="#1E1E1E")
style.configure("BG.TLabel", padding=6, relief="flat5", foreground="#D4D4D4", background="#1E1E1E")
style.configure("Ent.TLabel", padding=6, relief="flat5", foreground="#D4D4D4", background="#1E1E1E")
style.configure("Btn.TLabel", padding=6, relief="flat5", foreground="#D4D4D4", background="#444", anchor = tk.CENTER)
style.map("Btn.TLabel", background=[('pressed', '!disabled', '#666'), ('active', '#4D4D4D')])

frame.rowconfigure(0, weight = 1)
frame.columnconfigure(0, weight = 1)
ttk.Label(frame, style="BG.TLabel", justify = tk.RIGHT).grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=2,
    pady=2
)
_field = ttk.Entry(frame, text="Span 4 columns", style="Ent.TLabel", justify = tk.RIGHT, font=("Helvetica 32 bold"), validate="key")
_field.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=20,
    pady=2
)
#_field['validatecommand'] = (_field.register(testVal),'%P','%d')

for row in range(1, 7):
    frame.rowconfigure(row, weight = 1)
    for col in range(4):
        frame.columnconfigure(col, weight = 1)
        _btn = ttk.Button(
            frame,
            text=f"Cell ({row}, {col})",
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
root.resizable(True, True)

root.mainloop()