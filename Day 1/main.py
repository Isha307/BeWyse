from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Friends!!"

@app.route('/check/<int:n>')
def check(n):
    if(n%2==0):
        result = [{
            "check": "Even",
            "number": n,
        }]
    else:
        result =[ {
            "check": "Odd",
            "number": n,
        }]
    return jsonify(result)

app.run()