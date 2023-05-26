from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(),Email()])
    password = PasswordField(label='password', validators=[DataRequired(),Length(min=8,max=36)])
    submit = SubmitField(label='Login')




app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "mysercretkey"
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if request.method == 'GET':
        login_form.validate_on_submit()
        print(login_form.errors)
        return render_template('login.html',form=login_form)
    else:
        if request.method == "POST":
            login_form.validate_on_submit()
            print(login_form.errors)
            if login_form.validate_on_submit():
                app.logger.info(request.form['email'])
                app.logger.info(request.form['password'])
            if login_form.validate():
                if login_form.email.data == "admin@email.com" and login_form.password.data == "123456789":
                    # return "<h1>Welcome</h1><img src='https://media1.giphy.com/media/3q0gmyAwlORKgfLPS1/giphy.gif?cid=ecf05e47oddolg7znx0woobdi7ft8mts58b13jxhuhdgmyrz&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
                    return render_template('success.html')
                else:
                    # return "<h1>Access Denied</h1><img src='https://media4.giphy.com/media/l0ErQ2UfBNFEIlqjC/giphy.gif?cid=ecf05e47q36ft0fgixowb7qsnx0cqi6jv7l9n80x6nvb0m1v&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
                    return render_template('denied.html')
            else:
                return render_template('login.html',form=login_form)


if __name__ == '__main__':
    app.run(debug=True)