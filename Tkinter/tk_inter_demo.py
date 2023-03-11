#tk documentaion https://tcl.tk/man/tcl8.6/TkCmd/contents.htm

import tkinter


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height=500)

#creating label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, 'normal'))
#pack method adds the component to the centre of the screen
my_label.pack(side="top")

my_label.config(text="New Text")

def button_click():
    my_label.config(text="Button clicked")
    print("Button clicked")

def reset_text():
    my_label.config(text="New text")

def change_label():
    my_label.config(text=f"{text_input.get()}", font=("Times New Roman",50,"italic"))

def spinbox_get():
    print(spinbox.get())

def scale_value(value):
    print(value)
    my_label.config(font=("Times New Roman",value,'bold'))

def checkbutton_checked():
    if checked_state.get() == 1:
        label_for_checkbutton.config(text="Checkbutton checked")
        print("Check button is checked")
        print(checked_state.get())
    else:
        label_for_checkbutton.config(text="Checkbutton unchecked")
        print("Check button is unchecked")
        print(checked_state.get())

def radio_used():
    print(radio_state.get())

def listbox_used(event):
    print(list_box.get(list_box.curselection()))

button = tkinter.Button(text="Click me!", command=button_click)
button.pack()
reset_button = tkinter.Button(text="reset", command=reset_text, width=6)
reset_button.pack()


text_input = tkinter.Entry(width=10)
text_input.insert(tkinter.END ,"Some text")
text_input.pack()

submit_button = tkinter.Button(text="submit" , width = 6, command=change_label)
submit_button.pack()

text_box = tkinter.Text(height = 5, width= 30)
text_box.insert(tkinter.END, "Example of multiline text box\nnew line \n new line")
text_box.focus()
print(text_box.get("1.0", tkinter.END))
text_box.pack()

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_get)
spinbox.pack()

scale = tkinter.Scale(from_=0, to=100 , command=scale_value, orient="horizontal")
scale.pack()

checked_state = tkinter.IntVar()
check_button = tkinter.Checkbutton(text="This is a check", variable=checked_state, command=checkbutton_checked)
check_button.pack()

label_for_checkbutton = tkinter.Label(text="Click the check button", font=("Arial",30,'normal'))
label_for_checkbutton.pack()

radio_state = tkinter.IntVar()
radiobutton_1 = tkinter.Radiobutton(text="Option 1", value=1,variable=radio_state, command = radio_used)
radiobutton_2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command= radio_used)
radiobutton_1.pack()
radiobutton_2.pack()

list_box = tkinter.Listbox(height=4)
fruits = ["Apple", "Banana", "Orange", "Pear"]
for item in fruits:
    list_box.insert(fruits.index(item), item)
list_box.bind("<<ListboxSelect>>", listbox_used)
list_box.pack()
    



window.mainloop()