from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "<b>"
    return wrapper

def make_italic(function):
    def wrapper():
        return "<i>" + function() + "<i>"
    return wrapper

def make_underline(function):
    def wrapper():
        return "<u>"+function()+"<u>"
    return wrapper

@app.route('/')
@make_bold
@make_italic
@make_underline
def hello_word():
    return 'hello world!'

@app.route('/bye')
def bye():
    return 'Bye!'

@app.route('/<name>')
def hello_user(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)