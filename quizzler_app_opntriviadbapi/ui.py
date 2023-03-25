from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUi:
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.score = self.quiz.score
        self.score_label = Label(text=f"Score : {self.score}", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.timer = None

        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,130,text="This is a sample text", font=('Arial',20,'italic'), fill="black", width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        
        
        self.true_image = PhotoImage(file="quizzler_app_opntriviadbapi/images/true.png")
        self.false_image = PhotoImage(file="quizzler_app_opntriviadbapi/images/false.png")

        self.false_button = Button(image=self.false_image, highlightthickness=0, bd=0, command=self.false_option)
        self.false_button.grid(row=2, column=0, padx=20, pady=20)

        self.true_button = Button(image=self.true_image, highlightthickness=0, bd=0, command=self.true_option)
        self.true_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()
        self.window.mainloop()

    
    def get_next_question(self):
        if self.timer != None:
            self.window.after_cancel(self.timer)
        self.change_canvas_bg_white()
        question_text_data = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question_text_data)


    def true_option(self):
        if self.quiz.check_answer("True"):
            self.change_canvas_bg_green()
            self.update_score_label()
        else:
            self.change_canvas_bg_red()
        if self.quiz.still_has_questions():
            self.timer = self.window.after(1000,self.get_next_question)
        else:
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")
            self.change_canvas_bg_white()
            self.canvas.itemconfig(self.question_text, text=f"Your score is {self.score}/10")
           


    def false_option(self):
        if self.quiz.check_answer("False"):
            self.change_canvas_bg_green()
            self.update_score_label()
        else:
            self.change_canvas_bg_red()

        if self.quiz.still_has_questions():

            self.timer = self.window.after(1000,self.get_next_question)
        else:
            self.change_canvas_bg_white()
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text=f"Your score is {self.score}/10")


    def update_score_label(self):
        self.score = self.quiz.score
        self.score_label.config(text=f"Score : {self.score}")


    def change_canvas_bg_green(self):
        self.canvas.configure(background="lightgreen")

    def change_canvas_bg_white(self):
        self.canvas.configure(background="white")

    def change_canvas_bg_red(self):
        self.canvas.configure(background="red")