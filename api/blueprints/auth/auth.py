from flask import request, flash
from flask import Blueprint
from flask_login import (
    login_required,
    login_user,
    current_user,
    logout_user)

from api.blueprints.user.models import User

user = Blueprint("user", __name__)


@user.route("/login", methods=["GET", "POST"])
def login():
    body = request.get_json(force=True)
    usr = User.find_by_identity(identity=body.get("email"))
    authorized = usr.authenticated(password=body.get("password"))
    if usr and authorized:
        return {"Success": "User logged on successfully"}, 200
    else:
        return {"error": "Email or password invalid"}, 401

@user.route('/signup', methods=['GET', 'POST'])
def signup():
    body = request.get_json(force=True)
    user = User(**body)
    user.encrypt_password(body.get("password"))
    user.save()
    id = user.id
    return {'id': str(id)}, 200

@user.route('/logout') 
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')