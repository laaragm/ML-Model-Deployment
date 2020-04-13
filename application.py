from flask import Flask, jsonify, request #import objects from the Flask model
import json

from train_and_predict import predict

#HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

app = Flask(__name__) #instantiates the app using Flask class

# @app.route('/') is called a route which is used to redirect the user to a specific page or perform 
# a particular function when the user visit's a particular URL; '/' means the home page 
@app.route('/', methods=['GET'])
def test():
    return jsonify({"message:": "It works"})

#POST request; data insertion
@app.route('/predict', methods=['POST'])
def predict_grade():
    data = request.get_json(force=True)
    print(jsonify(data))
    y_pred = predict(data)
    y_pred = float(y_pred)
    
    return jsonify({"NU_NOTA_MT:": y_pred})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True) 

"""
Make sure to not call your application flask.py because this would conflict with Flask itself.
You need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:
    $ export FLASK_APP=hello.py 
    $ flask run
    * Running on http://127.0.0.1:5000/

Alternatively you can use python -m flask:
    $ export FLASK_APP=hello.py
    $ python -m flask run
    * Running on http://127.0.0.1:5000/
"""
