from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.root_path}/cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/random", methods=['GET'])
def random_cafe():
    cafe_list = [item for item in db.session.query(Cafe).all()]
    random_cafe_choice = random.choice(cafe_list)
    return jsonify(name=random_cafe_choice.name, map=random_cafe_choice.map_url,
                    image_url = random_cafe_choice.img_url,
                    location = random_cafe_choice.location,
                    has_sockets = random_cafe_choice.has_sockets,
                    has_toilet = random_cafe_choice.has_toilet,
                    has_wifi = random_cafe_choice.has_wifi,
                    can_take_calls = bool(random_cafe_choice.can_take_calls),
                    seats = random_cafe_choice.seats,
                    coffee_price = random_cafe_choice.coffee_price
                   )


def make_json_response(cafe_list):
    res_obj = []
    for item in cafe_list:
        item_container_dict = dict()
        item_container_dict['name']=item.name 
        item_container_dict['map']=item.map_url
        item_container_dict['image_url'] = item.img_url
        item_container_dict['location'] = item.location
        item_container_dict['has_sockets'] = item.has_sockets
        item_container_dict['has_toilet'] = item.has_toilet
        item_container_dict['has_wifi'] = item.has_wifi
        item_container_dict['can_take_calls'] = bool(item.can_take_calls)
        item_container_dict['seats'] = item.seats
        item_container_dict['coffee_price'] = item.coffee_price
        wrapper_obj = dict()
        wrapper_obj['cafe'] = item_container_dict
        res_obj.append(wrapper_obj)
    return res_obj

@app.route("/all", methods=['GET'])
def all_cafes():
    cafe_list = [item for item in db.session.query(Cafe).all()]
    json_respose = make_json_response(cafe_list)
    return jsonify(json_respose)

@app.route("/search", methods=['GET'])
def search_cafe_location():
    cafe_list = [item for item in db.session.query(Cafe).all()]
    cafe_nearby = [item for item in cafe_list if item.location.casefold() == request.args.get("loc").casefold()]
    if len(cafe_nearby) > 0:
        return jsonify(make_json_response(cafe_nearby))
    else:
        return jsonify({"Not Found":"Sorry, no cafe's avalable at this location"})

    

## HTTP GET - Read Record

## HTTP POST - Create Record

@app.route("/add", methods=['POST'])
def add_cafe():
    can_take_calls = bool(request.form.get("can_take_calls"))
    name = request.form.get("name")
    print(request.form.get("name"))
    map_url = request.form.get("map_url")
    img_url = request.form.get("img_url")
    location = request.form.get("location")
    has_sockets = bool(request.form.get("has_sockets"))
    has_toilet = bool(request.form.get("has_toilet"))
    has_wifi = bool(request.form.get("has_wifi"))
    seats = request.form.get("seats")
    coffee_price = request.form.get("coffee_price")
    new_cafe = Cafe(name=name,
                    map_url=map_url,
                    img_url = img_url,
                    location = location,
                    has_sockets = has_sockets,
                    has_toilet = has_toilet,
                    has_wifi = has_wifi,
                    seats = seats,
                    coffee_price = coffee_price,
                    can_take_calls = can_take_calls)
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({'response' : {"success" : "Successfully added the new cafe" }})



## HTTP PUT/PATCH - Update Record

@app.route("/update_price/<int:id>", methods=['PATCH'])
def update_details(id):
    cafe_to_be_updated = db.session.query(Cafe).filter_by(id=id).first()
    if cafe_to_be_updated != None:
        if request.args.get("new-price") == None:
            new_price = request.form.get("new-price")
        else:
            new_price = request.args.get("new-price")
        # print(new_price)
        cafe_to_be_updated.coffee_price = new_price
        db.session.commit()
        return jsonify({"success" : "Price updated successfully"})
    else:
        return jsonify({"Error" : "Record not found, please check the id"}), 404


## HTTP DELETE - Delete Record

@app.route("/report-closed/<int:id>", methods=['DELETE'])
def report_closed(id):
    if request.args.get("api-key") == "MySecretApiKey":
        cafe_obj_to_delete = db.session.query(Cafe).filter_by(id=id).first()
        if cafe_obj_to_delete != None:
            db.session.delete(cafe_obj_to_delete)
            db.session.commit()
            return jsonify({"success" : "Cafe closure reported success"})
        else:
            return jsonify({"Error":"Cafe not found, check the id"}),404
    else:
        return jsonify({'Error' : "Invalid key"}), 404

#https://documenter.getpostman.com/view/27752549/2s93sW7unp


if __name__ == '__main__':
    app.run(debug=True)
