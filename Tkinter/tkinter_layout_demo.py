from tkinter import *

window = Tk()
window.title("Layout Demo")
window.minsize(width=500, height=500)
window.config(padx=150, pady=150)

def button_clicked():
    print("Button clicked")

label = Label(text="New Label", font=("Arial", 25, 'normal'))
# label.pack()
label.grid(row=0, column=0)

button = Button(text="Click me!", command=button_clicked)
# button.pack()
button.grid(row=1, column=1)

entry = Entry(width= 10)
print(entry.get())
# entry.pack()
entry.grid(row=2, column=3)

new_buttton = Button(text="New Button", command=button_clicked)
new_buttton.grid(row=0, column=2)

window.mainloop()
