from tkinter import *
import requests


def get_quote():
    data = requests.get(url="https://api.kanye.rest")
    data.raise_for_status()
    data_as_json = data.json()
    canvas.itemconfig(quote_text, text=data_as_json.get("quote"))




window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, background="white")

canvas = Canvas(width=300, height=414, background="white", highlightthickness=0)
background_img = PhotoImage(file="kanye-quotes/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye-quotes/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0,bd=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()