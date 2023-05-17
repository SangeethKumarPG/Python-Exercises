from flask import Flask,render_template
import datetime
import random
import requests

app=Flask(__name__)
@app.route("/")
def home():
    random_number = random.randint(1,9)
    date = datetime.date.today()
    year = date.year
    return render_template('index.html',number=random_number,year=year)


@app.route("/guess/<name>")
def guess(name):
    params={
        "name" : name
    }
    response = requests.get(url="https://api.agify.io", params=params)
    json_response_agify = response.json()
    age = json_response_agify.get("age")
    genderize_param = {
        "name" : name
    }
    genderize_response = requests.get(url="https://api.genderize.io",params=genderize_param)
    gender_json = genderize_response.json()
    gender = gender_json.get("gender")
    return render_template('gender.html',age=age,name=name,gender=gender)

@app.route("/blog")
def get_blog():
    response = requests.get("https://api.npoint.io/66a01db051fc5b17179b")
    all_posts = response.json()
    return render_template('blog.html',posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)