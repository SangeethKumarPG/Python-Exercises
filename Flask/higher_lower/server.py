from flask import Flask
import random
app = Flask(__name__)

RANDOM_NUMBER = 0
def set_random_number():
    global RANDOM_NUMBER
    RANDOM_NUMBER = random.randint(0,9)

@app.route("/")

def home_page():
    set_random_number()
    return "<h1>Guess a number between 0 and 9</h1>"\
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/<int:number>")
def higher_lower(number):
    # print(f"Number is {number}")
    global RANDOM_NUMBER
    correct_number = RANDOM_NUMBER
    if number > correct_number:
        return "<h1 style='color:red'>Too high</h1><br>"\
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif number < correct_number:
        return "<h1 style='color:red'>Too Low</h1><br>"\
        "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number==correct_number:
        return "<h1 style='color:green'>You Found Me!</h1><br>"\
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

if __name__ == "__main__":
    app.run()