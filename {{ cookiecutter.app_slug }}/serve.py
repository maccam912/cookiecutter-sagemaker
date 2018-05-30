from flask import Flask
from flask import request
from flask import g
import pickle
application = Flask(__name__)

@application.before_request
def add_model_to_globals():
    g.model = pickle.load(open("/opt/ml/model/model.pkl", "rb"))

@application.route("/ping", methods=['GET'])
def ping():
    return "pong"

@application.route("/invocations", methods=['POST'])
def invocations():
    return g.model.invoke(request.data)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
