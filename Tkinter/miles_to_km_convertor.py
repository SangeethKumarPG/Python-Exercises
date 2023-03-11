from tkinter import *

window = Tk()
window.minsize(width=300, height=100)
window.title("Miles to Kilometre Converter")
window.config(padx=20, pady=20)
window.resizable(width=False, height=False)


def convert_miles_to_km():
    miles = float(user_input.get())
    km_value = round(miles * 1.609, 2)
    output_in_km_label.config(text=f"{km_value}")

user_input = Entry(width=10)
user_input.grid(row=0, column=1)


label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)
label_miles.config(padx=5, pady=5)

equals_label = Label(text="is equal to")
equals_label.grid(row=1, column=0)
equals_label.config(padx=5, pady=5)

output_in_km_label = Label(text="0")
output_in_km_label.grid(row=1, column=1)
output_in_km_label.config(padx=5, pady=5)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)
km_label.config(padx=5, pady=5)

submit_button = Button(text="Calculate", command=convert_miles_to_km)
submit_button.grid(row=2, column=1)
# submit_button.config(padx=5, pady=5)


window.mainloop()


