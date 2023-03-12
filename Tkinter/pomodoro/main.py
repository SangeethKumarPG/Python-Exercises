from tkinter import *
import math
#colorhunt.io for color palette
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    check_mark_label.config(text="")
    main_label.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global SHORT_BREAK_MIN
    global LONG_BREAK_MIN
    global WORK_MIN
    reps += 1
    # print(reps)
    if reps % 2 != 0:
        main_label.config(text="Work" , fg=GREEN, font=(FONT_NAME,45,'bold'), bg=YELLOW)
        count_down(WORK_MIN * 60)
        # print("work")
    elif reps % 8 == 0:
        main_label.config(text="Long Break" , fg=RED, font=(FONT_NAME,45,'bold'), bg=YELLOW)
        count_down(LONG_BREAK_MIN * 60)
        # print("long break")
    else:
        main_label.config(text="Short Break" , fg=PINK, font=(FONT_NAME,45,'bold'), bg=YELLOW)
        count_down(SHORT_BREAK_MIN * 60)
        # print("break")
    # reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if int(count_sec) == 0:
        count_sec = "00"
    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000,count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            num_of_checks = int(reps/2)
            output = num_of_checks * "✔"
            check_mark_label.config(text=output)
             
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=15, bg=YELLOW)

main_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME,45,'bold'), bg=YELLOW)
main_label.grid(row=0, column=1)

canvas = Canvas(width= 200, height=224, bg=YELLOW, highlightthickness=0)
background_image = PhotoImage(file = "Tkinter/pomodoro/tomato.png")
canvas.create_image(100, 112, image = background_image)
timer_text = canvas.create_text(100,125, text="00:00", fill="white", font=(FONT_NAME,35,'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", fg=RED, background=YELLOW, font=('Arial',20,'normal'), highlightthickness=0, border=0, command=start_timer)
start_button.grid(row = 2, column=0)

reset_button = Button(text="Reset", fg=RED, background=YELLOW, font=('Arial',20,'normal'), highlightthickness=0, border=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark_label = Label(text="", fg=GREEN, background=YELLOW)
check_mark_label.grid(row=3, column=1)

window.mainloop()