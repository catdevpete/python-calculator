from tkinter import * 
from tkinter.ttk import * 
from time import strftime

root = Tk()
root.title("Calculator")
root.configure(background='#1E1E1E')

root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)

frame = Frame(root)
frame.grid(row=0, column=0, sticky = NSEW)

#frame.rowconfigure(0, weight = 1)
#frame.columnconfigure(0, weight = 1)
#frame.columnconfigure(1, weight = 2)

style = Style()
style.theme_use('clam')
style.configure("TFrame", background="#1E1E1E")
style.configure("TLabel",foreground="#D4D4D4", background="#1E1E1E")
style.configure("Ent.TLabel", relief="solid", foreground="#D4D4D4", background="#444")
style.configure("Btn.TLabel", padding=6, relief="flat5", foreground="#D4D4D4", background="#444")
style.map("Btn.TLabel", background=[('pressed', '!disabled', '#666'), ('active', '#4D4D4D')])

frame.rowconfigure(0, weight = 4)
frame.columnconfigure(0, weight = 1)
Button(frame, text="Span 4 columns", style="Btn.TLabel").grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=2,
    pady=2
)

for row in range(1, 7):
    frame.rowconfigure(row, weight = 1)
    for col in range(4):
        frame.columnconfigure(col, weight = 1)
        _btn = Button(
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