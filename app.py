from flask import Flask, jsonify
from flask_cors import cross_origin

app = Flask(__name__)

@app.route("/")
@cross_origin()
def index():
    return "Please select route for api!"

@app.route("/api1")
@cross_origin()
def api1():
    return jsonify({'test': 'case1'})

@app.route("/api2")
@cross_origin()
def api2():
    return jsonify({'k1': 'case1', 'k2': 'case2', 'k3': 'case3'})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=4973)