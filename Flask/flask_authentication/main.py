from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, fresh_login_required

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.root_path}/users.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    with app.app_context():
        return db.session.get(entity = User, ident=user_id)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    if request.method == 'POST':
        if not db.session.query(User).filter_by(email = request.form['email']).first():
            new_user = User(
                email = request.form['email'],
                password = generate_password_hash(request.form['password'],'pbkdf2:sha256',salt_length=8),
                name = request.form['name']
            )
            db.session.add(new_user)
            db.session.flush()
            id = new_user.id
            db.session.commit()
            return redirect(url_for('secrets',id=id))
        else:
            flash("User with email already exists","errors")
            return redirect(url_for('register'))


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = db.session.query(User).filter_by(email=request.form['email']).first()
        if user:
            if check_password_hash(user.password,request.form['password']):
                login_user(user)
                # print(user.is_authenticated)
                return redirect(url_for('secrets',id=user.id))
            else:
                flash("Incorrect Password","errors")
                return redirect(url_for('login'))
        else:
            flash("User not found","errors")
            return redirect(url_for('login'))
    return render_template('login.html')



@app.route('/secrets/<int:id>')
@login_required
def secrets(id):
    user = db.session.query(User).filter_by(id=id).first()
    name = user.name
    return render_template("secrets.html",name = name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route('/download')
@login_required
def download():
    if current_user.is_authenticated:
        return send_from_directory(directory=f"{app.root_path}/static/files",path='cheat_sheet.pdf',as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
