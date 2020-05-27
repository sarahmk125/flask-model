import logging

from app import auth
from app import db
from app.models.users import User
from flask_login import login_user, logout_user, login_required
from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash


@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    # Make values required
    email = request.form.get('email')
    password = request.form.get('password')

    logging.info(f'[Blueprint.Auth.login_post] Attempting to log in user {email}...')

    # Get the user and check if exists (they should, on login) and check auth
    user = User.query.filter_by(email=email).first()
    if password and user:
        password_check = check_password_hash(user.password, password)
    else:
        password_check = None

    if not user or not password_check:
        flash("Incorrect email or password.")
        return render_template('login.html')

    # Login successfull; actually login and go home
    login_user(user)
    return redirect(url_for('main.home'))


# @auth.route('/signup', methods=['GET'])
# def signup():
#     return render_template('signup.html')


# @auth.route('/signup', methods=['POST'])
# def signup_post():
#     # Make values required
#     email = request.form.get('email')
#     username = request.form.get('username')
#     password = request.form.get('password')

#     logging.info(f'[Blueprint.Auth.signup_post] Attempting to signup user {email}...')

#     # Check to see if the user already exists
#     if User.query.filter_by(email=email).first():
#         logging.info(f'[Blueprint.Auth.signup_post] User with email {email} already exists.')
#         flash('User under that email already exists.')
#         return redirect(url_for('auth.signup'))

#     # User does not exist under current email
#     new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))

#     db.session.add(new_user)
#     db.session.commit()

#     return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logging.info('[Blueprint.Auth.logout] Logging out current user...')

    logout_user()
    return redirect(url_for('auth.login'))
