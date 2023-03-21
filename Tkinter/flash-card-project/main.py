from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

#---------------------------- Reading Data From CSV----------------------------------#
try:
    words_dataframe = pandas.read_csv("Tkinter/flash-card-project/data/words_to_learn.csv")
except FileNotFoundError:
    words_dataframe = pandas.read_csv("Tkinter/flash-card-project/data/french_words.csv")
# word_dict = words_dataframe.to_dict()
#alternatively
word_dict = words_dataframe.to_dict(orient="records")
# print(word_dict)
random_card = {}


#---------------------------- Generating Random Words -------------------------------#
def choose_a_word():
    global random_card
    random_card = random.choice(word_dict)
    return random_card

def known_word():
    global word_dict, random_card
    try:
        word_dict.remove(random_card)
    except ValueError:
        pass
    generate_random_word()

def generate_random_word():
    global word_dict
    global random_card
    global flip_timer
    # random_index = random.randint(0,100)
    # print(f"{word_dict['French'][random_index]} : {word_dict['English'][random_index]}")
    # text_canvas.itemconfig(word, text=f"{word_dict['French'][random_index]}")
    #alternatively
    window.after_cancel(flip_timer)
    
    random_card = choose_a_word()
    text_canvas.itemconfig(language,text="French", fill="black")
    text_canvas.itemconfig(word, text=f"{random_card['French']}", fill="black")
    text_canvas.itemconfig(background_image, image=front_card)
    # print(f"{random_card['French']} : {random_card['English']}")
    # print(len(word_dict))
    flip_timer = window.after(3000,func=flip_card)
    

    

#------------------------------ Flipping Card --------------------------------------#
def flip_card():
    global random_card, word_dict
    global flip_timer
    window.after_cancel(flip_timer)
    text_canvas.itemconfig(background_image,image=back_card)
    text_canvas.itemconfig(language, text="English", fill="white")
    text_canvas.itemconfig(word, text=f"{random_card['English']}", fill="white")
    flip_timer = window.after(3000,generate_random_word)
    try:
        # print(f"Removing random card {random_card}")
        word_dict.remove(random_card)
    except ValueError:
        pass

    


#------------------------------- UI ------------------------------------------------#
window = Tk()
window.title("Flash card app")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)



front_card = PhotoImage(file="Tkinter/flash-card-project/images/card_front.png")
back_card = PhotoImage(file="Tkinter/flash-card-project/images/card_back.png")
text_canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
background_image = text_canvas.create_image(400,265,image=front_card)
language = text_canvas.create_text(400,125,text="Tile", font=("Arial", 40, 'italic'), fill="black")
word = text_canvas.create_text(400,263, text="Word", fill="black", font=("Arial",60,"bold"))
text_canvas.grid(row=0, column=0, columnspan=2,padx=10, pady=10)

rigth_cover = PhotoImage(file="Tkinter/flash-card-project/images/right.png")
wrong_cover = PhotoImage(file="Tkinter/flash-card-project/images/wrong.png")

wrong_button = Button(image=wrong_cover, highlightthickness=0, bd=0, command=generate_random_word)
wrong_button.grid(row=1, column=0, padx=10)

right_button = Button(image=rigth_cover, highlightthickness=0, bd=0, command=known_word)
right_button.grid(row=1, column=1)


flip_timer = window.after(3000, func=generate_random_word)




window.mainloop()
unknown_words_df = pandas.DataFrame(word_dict)
# print(unknown_words_df)
unknown_words_df.to_csv("Tkinter/flash-card-project/data/words_to_learn.csv", index=False)
