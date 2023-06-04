from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime


## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
bootstrap = Bootstrap5(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.root_path}/posts.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = db.session.query(BlogPost).filter_by(id=index).first()
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/edit_post/<int:post_id>",methods=['GET','POST'])
def edit_post(post_id):
    if request.method == 'GET':
        form_to_populate = db.session.query(BlogPost).filter_by(id=post_id).first()
        edit_form = CreatePostForm(
            title = form_to_populate.title,
            subtitle = form_to_populate.subtitle,
            author = form_to_populate.author,
            img_url = form_to_populate.img_url,
            body = form_to_populate.body
        )
        return render_template('make-post.html', form=edit_form,id = post_id)
    if request.method == 'POST':
        edited_post = db.session.query(BlogPost).filter_by(id=post_id).first()
        edited_post.title = request.form['title']
        edited_post.subtitle = request.form['subtitle']
        edited_post.author = request.form['author']
        edited_post.img_url = request.form['img_url']
        edited_post.date = datetime.datetime.now().strftime("%d %B %Y")
        edited_post.body = request.form.get('body')
        db.session.commit()
        return redirect(url_for('get_all_posts'))


@app.route("/new-post", methods=['GET','POST'])
def new_post():
    form = CreatePostForm()
    if request.method == 'GET':
        return render_template('make-post.html',form=form)
    if request.method == 'POST':
        form.validate_on_submit()
        if form.validate():
            today = datetime.datetime.now()
            new_blog_post = BlogPost(
                title = request.form['title'],
                subtitle = request.form['subtitle'],
                author = request.form['author'],
                img_url = request.form['img_url'],
                date = today.strftime("%d %B %Y"),
                body = form.body.data
            )
            db.session.add(new_blog_post)
            db.session.commit()
            return redirect(url_for('get_all_posts'))
        else:
            return render_template('make-post.html',form=form)

@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.session.query(BlogPost).filter_by(id=post_id).first()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)