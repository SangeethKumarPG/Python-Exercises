from flask import Flask,render_template,request
import requests
import smtplib

USER_NAME = ""
PASSWORD = ""
app = Flask(__name__)

def send_email(name,email,phone,message):
    global USER_NAME,PASSWORD
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=USER_NAME, password=PASSWORD)
        connection.sendmail(from_addr=USER_NAME,
                            to_addrs="",
                            msg=f"subject:New Mesasge\n\nName : {name}\n Phone : {phone}\nEmail:{email}\nMessage:{message}")
    


def get_api_data():
    response = requests.get('https://api.npoint.io/1e3751e7e984715e9ffd')
    json_data = response.json()
    return json_data


@app.route("/")
def home():
    posts = get_api_data()
    return render_template('index.html',posts=posts)

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route('/contact', methods = ['GET','POST'])
def contact_page():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        app.logger.info("login success")
        print(f"{name},{email},{message}")
        send_email(name,email,phone,message)
        contact_response_message = "Successfully sent your message"
        return render_template('contact.html',contact_response_message=contact_response_message)
    else:
        contact_response_message = "Contact Me"
        return render_template('contact.html',contact_response_message=contact_response_message)

@app.route("/post/<int:id>")
def get_post(id):
    data = get_api_data()
    required_post = None
    for post in data:
        if post.get('id') == id:
            required_post = post
    if required_post != None:
        return render_template('post.html',post=required_post)
    

@app.route('/form-entry', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        app.logger.info("login success")
        print(f"{name},{email},{message}")
    return "<h1>Message Sent</h1>"

if __name__ == "__main__":
    app.run(debug=True)