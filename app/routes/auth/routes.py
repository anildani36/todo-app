from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import login_required, logout_user
from flask_pydantic import validate

from app.models.auth_models import LoginRequest, RegisterRequest
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.get('/login')
def show_login():
    return render_template("auth/login.html")


@auth_bp.post('/login')
@validate()
def login(form: LoginRequest):
    return AuthService.authenticate_user(form)


@auth_bp.get("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.show_login"))


@auth_bp.get('/register')
def show_register():
    return render_template("auth/register.html")


@auth_bp.post('/register')
@validate()
def register(form: RegisterRequest):
    if form.password != form.cpassword:
        flash("Passwords don't match")
        return redirect(url_for('auth.register'))
    return AuthService.register_user(form)


@auth_bp.post('/password_reset')
def password_reset():
    return "<h1>Password reset</h1>"
