from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    loaction_URL = StringField(label='Loaction URL',validators=[DataRequired()])
    open_time = StringField(label='Opening Time eg:8:00AM', validators=[DataRequired()])
    closing_time = StringField(label='Closing time eg:6:00PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices=[('✘','✘'),('☕️','☕️'), ('☕️☕️','☕️☕️'), ('☕️☕️☕️','☕️☕️☕️'), ('☕️☕️☕️☕️','☕️☕️☕️☕️'), ('☕️☕️☕️☕️☕️','☕️☕️☕️☕️☕️')], validators=[DataRequired()])
    wifi_rating = SelectField(label='Wifi Rating', choices=[('✘','✘'),('💪','💪'), ('💪💪','💪💪'), ('💪💪💪','💪💪💪'), ('💪💪💪💪','💪💪💪💪'), ('💪💪💪💪💪','💪💪💪💪💪')], validators=[DataRequired()])
    poweroutlet_rating = SelectField(label='Power Outlet Rating', choices=[('✘','✘'),('🔌','🔌'), ('🔌🔌','🔌🔌'), ('🔌🔌🔌','🔌🔌🔌'), ('🔌🔌🔌🔌','🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌','🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print("True")
            row = {
                'Cafe Name':form.cafe.data,
                'Location' : form.loaction_URL.data,
                'Open' : form.open_time.data,
                'Close' : form.closing_time.data,
                'Coffee' : form.coffee_rating.data,
                'Wifi' : form.wifi_rating.data,
                'Power' : form.poweroutlet_rating.data
            }
            print(row)
            with open('Flask/coffee_and_wifi/cafe-data.csv','a') as file:
                writer = csv.DictWriter(file, fieldnames=row.keys())
                writer.writerow(row)
            return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('Flask/coffee_and_wifi/cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            # print(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
