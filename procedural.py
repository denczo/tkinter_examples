from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

app = ThemedTk(theme="winxpblue")
app.title("Test")
app.geometry("600x600")
app.configure(bg='white')

packmanager = ttk.Frame(app)
gridmanager = ttk.Frame(app)


for x in range(9):
    label = ttk.Label(packmanager, text=x)
    label.pack(side=LEFT, fill='y', expand=True)

for x in range(9):
    label = ttk.Label(gridmanager, text=x)
    label.grid(row=x%3, column=x//3, ipadx=20, ipady=20, pady=2, padx=2)

packmanager.place(relx=0.5, rely=0.1, anchor="center")
gridmanager.place(relx=0.5, rely=0.5, anchor="center")

def action(message):
    button.config(text=message)

button = ttk.Button(app, text="Click me", command=lambda: action("Nice!"))
button.place(relx=0.5, rely=0.85, anchor="center", relwidth=0.5, relheight=0.3)

app.mainloop()