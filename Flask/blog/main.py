from flask import Flask, render_template
import post

app = Flask(__name__)
posts = None
@app.route('/')
def home():
    global posts
    posts = post.Post()
    all_posts = posts.get_all()
    return render_template("index.html",posts = all_posts)

@app.route("/post/<int:id>")
def show_post(id):
    current_post = posts.get_a_post(id)
    return render_template('post.html',current_post = current_post)


if __name__ == "__main__":
    app.run(debug=True)
