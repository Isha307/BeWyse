from flask import Flask, jsonify, abort

days = [
    {"id": 1, "name": "Monday"},
    {"id": 2, "name": "Tuesday"},
    {"id": 3, "name": "Wednesday"},
    {"id": 4, "name": "Thursday"},
    {"id": 5, "name": "Friday"},
    {"id": 6, "name": "Saturday"},
    {"id": 7, "name": "Sunday"},
]

app = Flask(__name__)

@app.route('/mm', methods = ["POST","GET"])
def success():
    return jsonify({"success": True}), 201

@app.route('/', methods = ['GET'])
def home():
    return jsonify("Hello Friends!!")

@app.route("/<int:day_id>", methods=["GET"])
def get_day(day_id):
    day = [day for day in days if day["id"] == day_id]
    print(day)
    if len(day) == 0:
        abort(404)
    return jsonify(day)




app.run()