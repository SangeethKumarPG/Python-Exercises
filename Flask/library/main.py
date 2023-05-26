from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("Flask/library/book-collections.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books(id INTGER PRIMARY KEY, title VARCHAR(250) NOT NULL UNIQUE, author VARCHAR(250) NOT NULL, rating FLOAT NOT NULL )")
# cursor.execute("INSERT INTO books VALUES(1,'Harry Potter','J.K Rowling',7.0)")
# db.commit()
# db.close()
db = SQLAlchemy()
app = Flask(__name__)
path = app.root_path
print(app.root_path)
app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///{app.root_path}/new-book-collections.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    title = db.Column(db.String, unique=True, nullable = False)
    author = db.Column(db.String, nullable = False)
    rating = db.Column(db.Float, nullable = False)

with app.app_context():
    db.create_all()
    # mybook = Book(title="Harry Potter Goblet of fire",
    #               author="J.K Rowling", rating = 7.5)
    # db.session.add(mybook)

    #Read
    # all_books = db.session.query(Book).all()
    # for book in all_books:
    #     print(book.title)

    #filter
    # particular_book = Book.query.filter_by(title = "Harry Potter Philosophers Stone").first()
    # print(particular_book.author)

    #Update
    # book_to_be_updated = db.session.query(Book).filter_by(id=1)
    # book_to_be_updated.title = "Updated Title"
    # book_to_be_updated.author = "Unknown author"

    #Delete
    # book_to_be_deleted = db.get_or_404(Book,2)
    # db.session.delete(book_to_be_deleted)
    # db.session.commit()




all_books = []


@app.route('/')
def home():
    global all_books
    all_books_from_db = db.session.query(Book).all()
    return render_template('index.html',books=all_books_from_db)


@app.route("/add", methods=['GET','POST'])
def add():
    global all_books
    if request.method == 'POST':
        book = dict()
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        book['title'] = title
        book['author'] = author
        book['rating'] = rating
        new_book = Book(title=title, author=author, rating= rating)
        db.session.add(new_book)
        db.session.commit()
        all_books.append(book)
        print(all_books)
    return render_template('add.html')

@app.route('/edit/<int:id>',methods = ['GET','POST'])
def edit(id):
    
    if request.method == 'GET':
        book_to_be_updated = db.session.query(Book).filter_by(id = id)
        return render_template('edit_rating.html',book = book_to_be_updated)
    if request.method == 'POST':
        book_to_be_updated = db.session.query(Book).filter_by(id = id).first()
        book_to_be_updated.rating = request.form['rating']
        print(request.form['rating'])
        print(f"Updated Rating = {book_to_be_updated.rating}")
        print("Here")
        db.session.commit()
        return redirect(url_for('home'))
    
@app.route('/delete/<int:id>',methods=['GET'])
def delete(id):
    book_to_be_deleted = db.session.query(Book).filter_by(id = id).first()
    db.session.delete(book_to_be_deleted)
    db.session.commit()
    return redirect(url_for('home'))


    


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

