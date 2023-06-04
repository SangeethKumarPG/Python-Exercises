from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired
import requests

TMDB_HEADER = {
    'accept' : 'application/json',
    'Authorization' : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNTBmMTBkNDMwOWQ4NmEwOThjMzg0MzU1MDVkNDUxNSIsInN1YiI6IjY0NzIyYjQ1YTE5OWE2MDEzMzI3ZTgxMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.iOjVHFJrC6UPkbz1XQHEfC9m-puyDhFABuZ4_VH1pjw"
}

TMDB_URL = "https://api.themoviedb.org/3/search/movie?"
TMDB_URL_WITH_ID = "https://api.themoviedb.org/3/movie/"
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{app.root_path}/movie-collection.db"  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String, unique = True, nullable = False)
    year = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(300), nullable = False)
    rating = db.Column(db.Float)
    review = db.Column(db.String(400))
    ranking = db.Column(db.Integer)
    image_url = db.Column(db.String(400))

class EditForm(FlaskForm):
    rating = DecimalField('Your rating out of 10 eg:7.5', validators=[DataRequired()])
    review = StringField('Your Review',validators=[DataRequired()])
    submit = SubmitField()

class AddMovie(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField()


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    # new_movie = Movie(
    # title="Phone Booth",
    # year=2002,
    # description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    # rating=7.3,
    # ranking=10,
    # review="My favourite character was the caller.",
    # image_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()
    # db.session.close()
    all_movies = db.session.query(Movie).order_by(Movie.rating.asc())
    # print(f"Length of movies : {all_movies.count()}")
    count = all_movies.count()
    for movie in all_movies:
        movie.ranking = count
        count -= 1
        db.session.commit()
    return render_template("index.html",movies = all_movies)


@app.route("/edit/<int:id>", methods=['GET','POST'])
def edit(id):
    edit_form = EditForm()
    current_movie = db.session.query(Movie).filter_by(id=id)
    if request.method == 'GET':
        return render_template('edit.html',movie = current_movie, form=edit_form)
    if request.method == 'POST':
        if edit_form.validate_on_submit():
            current_movie = db.session.query(Movie).filter_by(id=id).first()
            current_movie.rating = request.form['rating']
            current_movie.review = request.form['review']
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return render_template('edit.html',movie = current_movie, form=edit_form)


@app.route("/delete/<int:id>")
def delete(id):
    current_movie = db.session.query(Movie).filter_by(id=id).first()
    db.session.delete(current_movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['GET','POST'])
def add():
    add_movie_form = AddMovie()
    if request.method == 'GET':
        return render_template('add.html',form=add_movie_form)
    if request.method =='POST':
        title_name = request.form['title']
        req_param = {
            "query" : title_name,
            "include_adult" : True,
            "language" : 'en-US',
            'page' : 1
        }
        response = requests.get(url=TMDB_URL, headers=TMDB_HEADER, params=req_param)
        movie_api_response = response.json()
        search_result = movie_api_response.get('results')
        return render_template('select.html',results = search_result)


@app.route('/select/<int:id>', methods=['GET'])
def select(id):
    req_param = {
            "language" : 'en-US'
    }
    response = requests.get(url=f"{TMDB_URL_WITH_ID}{id}", params=req_param, headers=TMDB_HEADER)
    movie_reponse = response.json()
    title = movie_reponse.get('original_title')
    poster = "https://image.tmdb.org/t/p/w500"+movie_reponse.get('poster_path')
    year = movie_reponse.get('release_date').split('-')[0]
    description = movie_reponse.get('overview')
    new_movie = Movie(
            title = title,
            year = year,
            description = description,
            image_url = poster
        )
    db.session.add(new_movie)
    db.session.flush()
    insertion_id = new_movie.id
    db.session.commit()
    return redirect(url_for('edit', id=insertion_id))



if __name__ == '__main__':
    app.run(debug=True, use_reloader = False)
