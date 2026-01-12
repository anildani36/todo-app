from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.get('/login')
def show_login():
    return render_template("auth/login.html")

@auth_bp.post('/login')
def login():
    # Update logic here
    return "Profile Updated!"

@auth_bp.get('/register')
def show_register():
    return render_template("auth/register.html")


@auth_bp.post('/register')
def register():
    # Update logic here
    return "Profile Updated!"