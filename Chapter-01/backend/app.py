from flask import Flask, request, Response, json
from flask_mongoengine import MongoEngine

from models import User

app = Flask(__name__)

app.config["MONGODB_DB"] = "web_sec"
app.config["MONGODB_HOST"] = "127.0.0.1"
app.config["MONGODB_PORT"] = 27017
app.config["MONGODB_CONNECT"] = False

db = MongoEngine()
db.init_app(app)


@app.route('/')
def home():
    return 'Home!'


@app.route('/sign-in', methods=['POST'])
def auth():
    email = request.json.get('email')

    if not email:
        return Response(json.dumps({"message": "No Email"}), mimetype="application/json", status=400)

    password = request.json.get('password')

    if not password:
        return Response(json.dumps({"message": "No Password"}), mimetype="application/json", status=400)

    user = User.objects(email=email, password=password)

    if not user:
        return Response(json.dumps({"message": "Unauthorized"}), mimetype="application/json", status=401)

    return Response(json.dumps({"message": "Sign In Successful"}), mimetype="application/json")


@app.route('/sign-up', methods=['POST'])
def auth():
    email = request.json.get('email')

    if not email:
        return Response(json.dumps({"message": "No Email"}), mimetype="application/json", status=400)

    password = request.json.get('password')

    if not password:
        return Response(json.dumps({"message": "No Password"}), mimetype="application/json", status=400)

    user = User(email=email, password=password)
    user.save()

    return Response(json.dumps({"message": "Sign Up Successful"}), mimetype="application/json")


if __name__ == '__main__':
    app.run()
