from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
from .models import User

auth = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
        try:
            email_exist = db.session.query(User).where(User.email == email).scalar()
            username_exist = db.session.query(User).where(User.username == username).scalar()
        except:
            pass
        else:            
            if username_exist:
                flash("Username already taken.", category="danger")
            elif email_exist:
                flash("Email address is already registered!", category="danger")
            else:
                new_user = User(username=username,
                                email=email,
                                password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                return redirect(url_for('views.home'))
    return render_template("signup.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = db.session.query(User).where(User.username == username).scalar()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password.", category="danger")
        else:
            flash("User not registered.", category="danger")
    return render_template("login.html")

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('views.home'))