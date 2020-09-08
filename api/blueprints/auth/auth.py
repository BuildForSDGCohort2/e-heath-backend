from flask import request, jsonify
from flask import Blueprint

from api.blueprints.user.models import User

user = Blueprint("user", __name__)


@user.route("/login", methods=["GET", "POST"])
# @anonymous_required()
def login():
    body = request.get_json(force=True)
    usr = User.find_by_identity(identity=body.get("email"))
    authorized = usr.authenticated(password=body.get("password"))
    if usr and authorized:
        return {"Success": "User logged on successfully"}, 200
    else:
        return {"error": "Email or password invalid"}, 401


# @user.route('/login', methods=['GET', 'POST']) # HTTP request methods namely "GET" or "POST"
# def login():
#     data = []
#     if request.method == 'POST': # Checks if it's a POST request
#         data = [dict(email=request.get_json()['email'], password='')] # Data structure of JSON format

#         response = jsonify(data) # Converts your data strcuture into JSON format
#         response.status_code = 202 # Provides a response status code of 202 which is "Accepted"

#         return response # Returns the HTTP response
#     else:
#         data = [dict(id='none', name='none', enmail='none')] # Data structure of JSON format
#         response = jsonify(data) # Converts your data strcuture into JSON format
#         response.status_code = 406 # Provides a response status code of 406 which is "Not Acceptable"

#         return response # Returns the HTTP response